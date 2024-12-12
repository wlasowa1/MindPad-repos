import RPi.GPIO as GPIO  #works only on Raspberry Pi hardware
import time

#GPIO setup
GPIO.setmode(GPIO.BCM)  #use BCM pin numbering

#define pins for buttons
pins = [22, 23, 24, 1, 7, 8, 17]  #buttons row 1 connected to pin 22, row 2 to pin 23, and row 3 to pin 24

#set up pins as inputs with pull-down resistors
for pin in pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print("Press a button to test...")

    while True:
        for pin in pins:
            if GPIO.input(pin) == GPIO.HIGH:  # Button is pressed
                print(f"Button on pin {pin} pressed")
                time.sleep(2)  # Debounce delay

finally:
    GPIO.cleanup()  #clean up GPIO pins
