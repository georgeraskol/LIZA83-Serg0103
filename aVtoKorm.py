import RPi.GPIO as GPIO  # Если вы используете Raspberry Pi
from time import sleep

# Настройка пинов
GPIO.setmode(GPIO.BCM)
motor_pin = 18  # Пин, к которому подключен мотор
sensor_pin = 23  # Пин, к которому подключен датчик уровня корма

# Инициализация пина мотора как выходного
GPIO.setup(motor_pin, GPIO.OUT)
pwm = GPIO.PWM(motor_pin, 50)  # ШИМ с частотой 50 Гц
pwm.start(0)  # Начальная скорость вращения двигателя равна нулю

# Инициализация пина датчика как входного
GPIO.setup(sensor_pin, GPIO.IN)

def feed():
    pwm.ChangeDutyCycle(100)  # Включаем двигатель на полную мощность
    sleep(5)  # Время кормления (в секундах)
    pwm.ChangeDutyCycle(0)  # Останавливаем двигатель

try:
    while True:
        if GPIO.input(sensor_pin):  # Проверяем состояние датчика
            print("Кошка просит еду!")
            feed()
        else:
            print("Ждем...")
        sleep(1)  # Задержка между проверками состояния датчика
except KeyboardInterrupt:
    pwm.stop()  # Остановка ШИМ при прерывании программы
    GPIO.cleanup()  # Сброс настроек GPIO