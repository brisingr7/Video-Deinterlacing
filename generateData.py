########################## Functions ##############################

#Delete even rows
def del_even(image):
    image[::2] = 0
    return image

def del_odd(image):
    image[1::2] = 0
    return image

########################## Imports ###############################

import cv2
import numpy as np
import glob
from tqdm import tqdm

# read paths
video_paths = glob.glob("Videos/*/*.*", recursive=True)

#read videos

for video_path in tqdm(video_paths):
    ret, capture = cv2.VideoCapture(video)
    while ret :
        
