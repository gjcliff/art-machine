import RPi.GPIO as GPIO
import time

class A4988:
    def __init__(self, step, dir):
        self._step = step
        self._dir = dir
        #this variable is the length of the pulse sent to the step pin on the 
        #A4988 motor driver.
        self._snooze = 0.00005

    #getters
    def get_step(self):
        return self._step
    def get_dir(self):
        return self._dir
    def get_snooze(self):
        return self._snooze

    #setters
    def set_step(self, a):
        self._step = a
    def set_dir(self, a):
        self._dir = a
    def set_snooze(self,a):
        self._snooze = a

    #set the direction pin high, and complete one step.
    def turnCW(self,num_steps):
        GPIO.output(self._dir, GPIO.HIGH)
        for i in range(int(num_steps)):
            GPIO.output(self._step, GPIO.HIGH)
            time.sleep(self._snooze)
            GPIO.output(self._step, GPIO.LOW)

    #set the direction pin low, and complete one step.
    def turnCCW(self,num_steps):
        GPIO.output(self._dir, GPIO.LOW)
        for i in range(int(num_steps)):
            GPIO.output(self._step, GPIO.HIGH)
            time.sleep(self._snooze)
            GPIO.output(self._step, GPIO.LOW)