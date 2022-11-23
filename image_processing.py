import os
import numpy as np
from PIL import Image, ImageOps

def getcoords(fileName,thresh):
    script_dir = os.path.dirname(__file__)
    rel_path = fileName
    abs_file_path = os.path.join(script_dir, rel_path)

    #attempt to import the image
    try:
        im = Image.open(abs_file_path)
        im = ImageOps.exif_transpose(im)
        im = im.convert('L')
        
    except:
        return(print("couldn't open file"))
    
    # Resize image
    width, height = im.size
    if width > height:
        height = height*512/width
        width = 512
    else:
       width = width*512/height
       height = 512


    im = im.resize((int(width),int(height)), resample=Image.Resampling.BILINEAR)
    coords = np.array([[0,0]])
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            val = im.getpixel((x,y))
            if val < thresh:
                coords = np.append(coords,[[x,y]],axis=0)
    coords *= 2
    return(coords)