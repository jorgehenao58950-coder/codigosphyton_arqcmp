import RPi.GPIO as GPIO
import time

pinLed = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLed, GPIO.OUT)

led = GPIO.PWM(pinLed, 100)
led.start(100)

while True:
	for i in range (0, 100, 10):
		led.ChangeDutyCycle(i)
		time.sleep(0.1)

	time.sleep(1)

	for i in range(100, 0, -10):
		led.ChageDutyCycle(i)
		time.sleep(0.1)
	time.sleep(1)

