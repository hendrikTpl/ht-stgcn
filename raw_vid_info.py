from email import header
header.Header

import cv2
import os
import pandas as pd
import math

vid_path = "./../Dataset/vid/Video/"
vid_ext ="MTS"

file_name = []
info = []
for File in os.listdir(vid_path):
    if File.endswith(vid_ext):
        file_name.append(File)
    else:
        print("File with extention {} in Folder {} is not found".format(vid_ext, vid_path))

for i in range(len(file_name)):
    cap = cv2.VideoCapture(vid_path+file_name[i])
    #fps = int(math.ceil(cap.get(cv2.CAP_PROP_FPS)))      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = frame_count/fps
    minutes = duration/60
    seconds = duration%60
    info.append([file_name[i],fps, frame_count,duration,minutes, seconds])
    print("File: {} FPS: {} Total Frame: {} duration: {} minutes {} seconds".format(file_name[i],int(math.ceil(fps)), frame_count, round(minutes,3), round(seconds,3)))
    cap.release()

vid_info = pd.DataFrame(info)
vid_info.to_csv("raw_vid_info.csv",header=["File", "FPS", "Total Frame","Total Duration","Minutes","Seconds"], index=False)


    
