import threading
import time
import numpy as np
from A4988 import A4988
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib


class art_machine:
    def __init__(self, stepL, dirL, stepR, dirR):
        self._stepL = stepL
        self._dirL = dirL
        self._stepR = stepR
        self._dirR = dirR
        #self._snooze = 0.00001
        self._xLimit = 2
        self._yLimit = 3
        self._sleep = 24
        self._ms1 = 10
        self._ms2 = 9
        self._ms3 = 11
        self._motorL = A4988(stepL, dirL)
        self._motorR = A4988(stepR, dirR)
        self._28BYJpins = [4,14,15,18]
        self._28BYJ = RpiMotorLib.BYJMotor("sharpie","28BYJ")

    #getters
    def get_stepL(self):
        return self._stepL
    def get_dirL(self):
        return self._dirL
    def get_stepR(self):
        return self._stepR
    def get_dirR(self):
        return self._dirR

    #setters
    def set_stepL(self,a):
        self._stepL = a
    def set_dirL(self,a):
        self._dirL = a
    def set_stepR(self,a):
        self._stepR = a
    def set_dirR(self,a):
        self._dirR = a
    def set_image(self,a):
        self._image = a

    #moves the center motor carriage to the right using threading and returns
    #the position of the carriage after moving one step.
    def moveRight(self,motorxy):
        steps = 10
        thread1 = threading.Thread(target=self._motorL.turnCCW(steps))
        thread2 = threading.Thread(target=self._motorR.turnCCW(steps))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        motorxy[0] += 1
        return motorxy

    #moves the center motor carriage to the left using threading and returns
    #the position of the carriage after moving one step.
    def moveLeft(self,motorxy):
        steps = 10
        thread1 = threading.Thread(target=self._motorL.turnCW(steps))
        thread2 = threading.Thread(target=self._motorR.turnCW(steps))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        motorxy[0] -= 1
        return motorxy

    #moves the center motor carriage up using threading and returns
    #the position of the carriage after moving one step.
    def moveUp(self,motorxy):
        steps = 10
        thread1 = threading.Thread(target=self._motorL.turnCW(steps))
        thread2 = threading.Thread(target=self._motorR.turnCCW(steps))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        motorxy[1] += 1
        return motorxy

    #moves the center motor carriage down using threading and returns
    #the position of the carriage after moving one step.
    def moveDown(self,motorxy):
        steps = 10
        thread1 = threading.Thread(target=self._motorL.turnCCW(steps))
        thread2 = threading.Thread(target=self._motorR.turnCW(steps))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        motorxy[1] -= 1
        return motorxy
    
    #declare GPIO pin mode, set each pin as input or output, pull
    #microstepping pins (ms1, ms2, ms3) high.
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._xLimit, GPIO.IN)
        GPIO.setup(self._yLimit, GPIO.IN)
        GPIO.setup(self._sleep, GPIO.OUT)
        GPIO.setup(self._ms1, GPIO.OUT)
        GPIO.setup(self._ms2, GPIO.OUT)
        GPIO.setup(self._ms3, GPIO.OUT)
        GPIO.setup(self._stepL, GPIO.OUT)
        GPIO.setup(self._dirL, GPIO.OUT)
        GPIO.setup(self._stepR, GPIO.OUT)
        GPIO.setup(self._dirR, GPIO.OUT)

        GPIO.output(self._sleep, GPIO.HIGH)
        GPIO.output(self._ms1, GPIO.HIGH)
        GPIO.output(self._ms2, GPIO.HIGH)
        GPIO.output(self._ms3, GPIO.HIGH)

    def drawing(self,coords):
        print(f"coords size: {len(coords)}")
        print(f"coords: {coords}")
        try:
            self._28BYJ.motor_run(self._28BYJpins,.001,35,True,False,"half",0.001) #pulling the sharpie up 100 steps
            up = True #this variable is to keep track of whether the sharpie is up or down
            motorxy = np.zeros(2) #this keeps track of where the carriage actually is
            for i,xy in enumerate(coords):
                dirx = True if xy[0] > motorxy[0] else False #left is false, right is true
                diry = True if xy[1] > motorxy[1] else False #down is false, up is true
                #print(f"dirx = {dirx}, diry = {diry}")
                while motorxy[0] != xy[0]:
                    #print(f"here: 1")
                    #print(f"motorxy: {motorxy}, xy: {xy}")
                    motorxy = self.moveRight(motorxy) if dirx else self.moveLeft(motorxy)
                while motorxy[1] != xy[1]:
                    #print(f"here: 2")
                    #print(f"motorxy: {motorxy}, xy: {xy}")
                    motorxy = self.moveUp(motorxy) if diry else self.moveDown(motorxy)
                #if up == True and i != 0:
                    #self._28BYJ.motor_run(self._28BYJpins,0.001,35,False,False,"half",0.001)
                    #up = False
                if i < len(coords)/2 - 1:
                    if xy[0] == coords.index(i+1, 0) and abs(xy[1] - coords.index(i+1,1)) <= 2:
                        #print(f"here: 3")
                        if up == True:
                            self._28BYJ.motor_run(self._28BYJpins,.001,35,False,False,"half",0.05)
                            time.sleep(0.005)
                            up = False
                    else:
                        if up == True:
                            #print(f"here: 5")
                            self._28BYJ.motor_run(self._28BYJpins,.001,35,False,False,"half",0.05)
                            self._28BYJ.motor_run(self._28BYJpins,.001,35,True,False,"half",0.05)
                        else:
                            #print(f"here: 6")
                            self._28BYJ.motor_run(self._28BYJpins,.001,35,True,False,"half",0.05)
                            up = True
            self._28BYJ.motor_run(self._28BYJpins,.001,35,True,False,"half",0.05)
            up = True
        except KeyboardInterrupt:
            GPIO.output(self._sleep, GPIO.LOW)
            GPIO.cleanup()
            exit(1)

    #def mouse(self):
    #    m = Controller()
    #    up = True
    #    self._28BYJ.motor_run(self._28BYJpins,0.00001,100,True,False,"full",0.01) #pulling the sharpie up 100 steps

        #gonna assume that I've already homed this thing
    #    prevcoords = [0, 0]
    #    
    #    def on_click(x,y,button,pressed):
    #        if pressed and up:
    #            self._28BYJ.motor_run(self._28BYJpins,0.00001,100,False,False,"full",0.01) #pulling the sharpie up 100 steps
    #            pressed = False
    #        elif not up:
    #            self._28BYJ.motor_run(self._28BYJpins,0.00001,100,True,False,"full",0.01) #pulling the sharpie up 100 steps

    #    listener = mouse.Listener(on_click=on_click)
    #    listener.start()

    #    while True:
    #        coords = m.position
    #        self.move(coords - prevcoords)
    #        prevcoords = coords