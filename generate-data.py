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
import time

np.random.seed(1337)

# read paths
video_paths = glob.glob("Videos/*/*.*", recursive=True)

#read videos

#counter
i = 0

for video_path in tqdm(video_paths):
    if np.random.uniform() > 0 :
        print(video_path)
        capture = cv2.VideoCapture(video_path)
        while capture.isOpened() :
            _ , frame = capture.read() # read frame

            try:
                if True : #Hack to reduce training samples (select 1/3rd of training images)
                    cv2.imwrite(f"dataset_new/ground_truth/1/{i}.bmp", frame) # write ground truth
                    #delete alternate even and odd rows
                    if i%2 == 0 :
                        frame = del_even(frame) #delete even rows
                    else:
                        frame = del_odd(frame) #delete odd

                    cv2.imwrite(f"dataset_new/interlaced/1/{i}.bmp", frame) #write interlaced frame

                    i += 1

            except Exception as e:
                print(e)
                break # this is stupid but it works

        capture.release()