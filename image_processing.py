import os
import numpy as np
import cv2 as cv

def getcoords(fileName):
    script_dir = os.path.dirname(__file__)
    rel_path = fileName
    abs_file_path = os.path.join(script_dir, rel_path)

    #attempt to import the image
    try:
        og = cv.imread(abs_file_path,0)
        r = 500.0 / og.shape[1]
        dim = (500, int(og.shape[0] * r))
        im = cv.resize(og, dim, interpolation=cv.INTER_AREA)
        # cv.imshow("og image", im)
        im = cv.medianBlur(im,5)
        
   
        im = cv.adaptiveThreshold(im,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        # cv.imshow("gaussian threshold", th)

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

    coords = np.array([[0,0]])
    for x,row in enumerate(im):
        for y,pixel in enumerate(row):
            if pixel == 255:
                coords = np.append(coords,[[x,y]],axis=0)
    #print(coords)
    coords *= 2
    return(coords)

#getcoords("wave.jpg")