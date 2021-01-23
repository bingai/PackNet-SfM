# https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/
# Steps:
#  Fetch all the image file names using glob
#  Read all the images using cv2.imread()
#  Store all the images into a list
#  Create a VideoWriter object using cv2.VideoWriter()
#  Save the images to video file using cv2.VideoWriter().write()
#  Release the VideoWriter and destroy all windows.

# Generate Video from images
import cv2
import numpy as np
import glob

import re
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


img_array = []
filenames = [filename for filename in glob.glob('./*.png')]
filenames.sort(key=numericalSort)
# sorted(filenames)
for filename in filenames:
    print(filename)
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('self_supervised_DDAD_384x640.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()