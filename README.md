# art-machine
I made this project to improve upon a similar project that I did for ENES351 in junior year of college at UMD.
The original idea for that project was to create a machine that could drag a sharpie across a piece of paper. It could only move the sharpie in the x and y directions, and was built in only 10 hours (in a row). It was controlled by the user with two pressure sensors.

This project uses the CoreXY cartesian motion system to move a sharpie around. It can automatically draw .jpg and .png files by turning the image to greyscale, and then recording the position of all points whose color value falls below a certain threshold.

I used 20mm v-rail to support the v-rail carriages. The two side carriages, middle carriage, motor mounts, and corner brackets were designed by me in Solidworks and printed on my Elegoo Neptune 3. I've included the .STL and .SLDPRT files in the CAD folder here.

I went through many iterations of CAD designs. My 3D printer was running constantly for about 2 weeks while I iterated through design improvements.
<p align="center"><img src="https://user-images.githubusercontent.com/94981561/200575872-2e9c3a1b-fe5c-4ed7-9787-68ea40e7cf82.JPG" width = "378" height ="504"></p>

Time and time again I would come home from work or wake up to prints that had messed up hours into their creation.
<p align="center"><img src="https://user-images.githubusercontent.com/94981561/200577570-50dd1717-f6b3-4e8c-8590-b3b4a6c68c76.JPG" width = "378 height = "504"></p>

A full look at the finished machine:
<p align="center"><img src="https://user-images.githubusercontent.com/94981561/200577580-a3f4f41a-a274-45ef-b7e1-21d0f95804dd.JPG" width = "378" height = "504"></p>
  
Here are some examples of pictures I've drawn with the machine:
original: Mona Lisa
<p align="center"><img src="https://user-images.githubusercontent.com/94981561/201396340-58af8680-1456-434a-9f61-3c708b5f4dcd.jpg" width "378" height = "504"></p>

machine drawn:
<p align="center"><img src="https://user-images.githubusercontent.com/94981561/201401130-dd30e56b-ca27-426b-bcd6-1fe93b589fc5.JPG" width "378" height = "504"></p>


original: The Great Wave of Kanagawa
<p align="center"><img src="https://user-images.githubusercontent.com/94981561/201399182-57b9f81e-5ee4-4983-a6c0-1a51b33ecb9d.jpg" width "378" height = "504"></p>

machine drawn:
<p align="center"><img src="https://user-images.githubusercontent.com/94981561/201399253-db6c8d45-6fff-4f5d-bc0d-426113ebff05.JPG" width "378" height = "504"></p>

original: On Demand Pharmaceuticals Logo
<p align="center"><img src="https://user-images.githubusercontent.com/94981561/201399300-26bbd772-ac1d-416f-a973-c76149fe8200.jpg" width "378" height = "504"></p>

machine drawn:
<p align="center"><img src="https://user-images.githubusercontent.com/94981561/201399325-875da682-23e0-4d64-916f-8903fe88b399.JPG" width "378" height = "504"></p>
 
list of libraries used:
  * numpy
  * PIL
  * RPi.GPIO
  * argparse
  * os, time, threading
