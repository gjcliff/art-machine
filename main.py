from art_machine import art_machine
import image_processing as im
import os
from PIL import Image
import RPi.GPIO as GPIO
import argparse

#setting up arguements
parser = argparse.ArgumentParser()
parser.add_argument("-t","--threshold",help="sets the threshold value for the script",default=100,type=int)
args = parser.parse_args()
threshold = args.threshold

#prompt the user for what file they'd like to open, restricted to files in the current directory with extension .jpg or .png
print('What file would you like to open?')
dir = os.listdir(os.path.dirname(__file__))

for name in dir:
    if any(x in name for x in [".jpg", ".png"]):
        print(name)

file = input()

#if the user doesn't specify a file, use wave.jpg
if file == "":
    file = "wave.jpg"

#convert png to jpg, if the user specified file is png
f, e = os.path.splitext(file)
outfile = f + ".jpg"
if file != outfile:
    try:
        with Image.open(file) as im:
            im.save(outfile)
            print(outfile)
    except OSError:
        print("cannot convert", file)

#use the image_processing script to convert the image to an 2D array of coordinates.
coords = im.getcoords(file,threshold)
print("coords: ",coords)

#declare art_machine object with RPI pin 17 as the left stepper motor step pin,
#RPI pin 27 as left stepper motor direction pin, RPI pin 22 as the right
#stepper motor step pin, and RPI pin 23 as the right stepper motor direction pin.
am = art_machine(17,27,22,23)
am.setup()

#begin drawing the picture.
am.drawing(coords)

#call GPIO cleanup to bring all the GPIO pins we're using to a low value.
GPIO.cleanup()
