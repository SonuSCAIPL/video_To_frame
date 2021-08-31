import cv2
import numpy as np

#READING video clip 
cap = cv2.VideoCapture('dir_path_of_video_clip')

count=0

while True:
    count+=1
    _, frame = cap.read()
    cv2.imwrite("frames/"+str(count)+".jpg",frame)
    #here frames/ is a folder name of my system, where vedio frames will be save 
    

    

