import os
import numpy as np
import cv2 as cv
from PIL import Image, ImageOps

def getcoords(fileName):
    script_dir = os.path.dirname(__file__)
    rel_path = fileName
    abs_file_path = os.path.join(script_dir, rel_path)

    #attempt to import the image
    try:
        og = cv.imread(abs_file_path,0)
        #og = ImageOps.exif_transpose(og)
        r = 500.0 / og.shape[1]
        dim = (500, int(og.shape[0] * r))
        im = cv.resize(og, dim, interpolation=cv.INTER_AREA)
        # cv.imshow("og image", im)
        im = cv.medianBlur(im,5)
        im = cv.adaptiveThreshold(im,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, .5)
        # cv.imshow("gaussian threshold", im)

        # cv.waitKey(0)
        # cv.destroyAllWindows()
        # exit()
      
    except:
        return(print("couldn't open file"))
    
    # Resize image
    # width, height = im.size
    # if width > height:
    #     height = height*512/width
    #     width = 512
    # else:
    #    width = width*512/height
    #    height = 512

    #coords = np.array([[0,0]])
    #print(im.shape)
    im = cv.rotate(im,cv.ROTATE_90_COUNTERCLOCKWISE)
    im = cv.flip(im,1)
    #im = np.array(im)
    #print(im.shape)
    coords = np.argwhere(im == 0)
    #coords = np.array(coords)
    # print(coords,coords.size)
    coords *= 2
    #print(coords)
    return(coords)

# getcoords("mona-lisa.jpg")