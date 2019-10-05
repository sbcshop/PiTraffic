import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


pin_dict = {"South": (17, 27, 22),
			"East": (16, 20, 21),
			"North": (5, 6, 13),
			"West": (23, 24, 25)
			}

for direction in pin_dict:
    for pin in pin_dict[direction]:
        GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin_dict[direction][0], GPIO.HIGH)

try:
	while True:
		for direction in pin_dict:
			GPIO.output(pin_dict[direction][0], GPIO.LOW)
			GPIO.output(pin_dict[direction][1], GPIO.HIGH)
			sleep(1)
			GPIO.output(pin_dict[direction][1], GPIO.LOW)
			GPIO.output(pin_dict[direction][2], GPIO.HIGH)
			sleep(3)       
			GPIO.output(pin_dict[direction][2], GPIO.LOW)       
			GPIO.output(pin_dict[direction][0], GPIO.HIGH)       
except KeyboardInterrupt:
	GPIO.cleanup()
