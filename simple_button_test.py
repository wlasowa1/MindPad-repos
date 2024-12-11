import RPi.GPIO as GPIO  #works only on Raspberry Pi hardware
import time

#GPIO setup
GPIO.setmode(GPIO.BCM)  #use BCM pin numbering

#define pins for buttons
pins = [22, 23, 24]  #buttons row 1 connected to pin 22, row 2 to pin 23, and row 3 to pin 24

#set up pins as inputs with pull-up resistors
for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("press a button to test...")

    while True:
        for pin in pins:
            if GPIO.input(pin) == GPIO.LOW:  #button is pressed
                print(f"button on pin {pin} pressed")
                time.sleep(0.2)  #debounce delay

finally:
    GPIO.cleanup()  #clean up GPIO pins
