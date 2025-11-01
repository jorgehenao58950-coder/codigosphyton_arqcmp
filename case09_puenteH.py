import RPi.GPIO as GPIO
from time import sleep

PIN_IN1 = 7
PIN_IN2 = 11
PIN_IN3 = 13
PIN_IN4 = 15
PIN_ENA = 32
PIN_ENB = 33

maxSpeed = 100
minSpeed = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)
GPIO.setup(PIN_IN3, GPIO.OUT)
GPIO.setup(PIN_IN4, GPIO.OUT)
GPIO.setup(PIN_ENA, GPIO.OUT)
GPIO.setup(PIN_ENB, GPIO.OUT)

motorIzq = GPIO.PWM(PIN_ENA, maxSpeed)
motorDer = GPIO.PWM(PIN_ENB, maxSpeed)

motorIzq.start(maxSpeed)
motorDer.start(maxSpeed)

while True:
    motorIzq.ChangeDutyCycle(maxSpeed)
    motorDer.ChangeDutyCycle(maxSpeed)

    GPIO.output(PIN_IN1, True)
    GPIO.output(PIN_IN2, False)
    GPIO.output(PIN_IN3, True)
    GPIO.output(PIN_IN4, False)
