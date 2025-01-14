import RPi.GPIO as GPIO
from time import sleep

# Указываем режим нумерации контактов (BCM)
GPIO.setmode(GPIO.BCM)

# Определяем номера пинов для каждого светодиода
red_pin = 17
yellow_pin = 27
green_pin = 22

# Устанавливаем пины как выходы
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

try:
    while True:
        # Красный свет
        GPIO.output(red_pin, GPIO.HIGH)
        sleep(10)  # Держим красный свет включенным 10 секунд

        # Желтый свет
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.HIGH)
        sleep(3)  # Держим желтый свет включенным 3 секунды

        # Зеленый свет
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)
        sleep(15)  # Держим зеленый свет включенным 15 секунд

        # Выключение зеленого света перед следующим циклом
        GPIO.output(green_pin, GPIO.LOW)
except KeyboardInterrupt:
    # Очищаем пины при завершении программы
    GPIO.cleanup()