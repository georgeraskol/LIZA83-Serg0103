import RPi.GPIO as GPIO
from time import sleep
import schedule
import datetime

# Настройка режима нумерации пинов
GPIO.setmode(GPIO.BCM)

# Определение пина для кнопки
button_pin = 23
# Определение пина для сервопривода
servo_pin = 18

# Инициализация пинов
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo_pin, GPIO.OUT)

# Частота сигнала для сервопривода
pwm_frequency = 50  # Hz

# Создание объекта PWM
pwm = GPIO.PWM(servo_pin, pwm_frequency)

# Функция для открытия кормушки
def feed():
    print(f"{datetime.datetime.now()} Открытие кормушки...")
    pwm.start(12.5)  # Угол поворота 180 градусов
    sleep(0.8)       # Время работы сервопривода
    pwm.ChangeDutyCycle(7.5)  # Возвращение в исходное положение
    sleep(0.8)
    pwm.stop()

# Функция для ручного кормления по кнопке
def manual_feed():
    if not GPIO.input(button_pin):
        feed()  # Запуск функции кормления при нажатии кнопки
        sleep(0.2)  # Небольшая задержка для предотвращения дребезга контактов

# Планирование автоматического кормления
def scheduled_feed():
    print(f"{datetime.datetime.now()} Автоматическое кормление")
    feed()

# Установка времени кормления
schedule.every().day.at("09:00").do(scheduled_feed)  # Кормление в 9 утра
schedule.every().day.at("21:00").do(scheduled_feed)  # Кормление в 9 вечера

try:
    while True:
        manual_feed()  # Проверяем кнопку
        schedule.run_pending()  # Проверяем расписание
        sleep(1)  # Задержка перед следующей итерацией

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()