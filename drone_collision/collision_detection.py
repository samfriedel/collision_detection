"""
Script to detect a collision between a drone and a ball
 1. detect drone and create bounding box
 2. detect ball and create bounding box
 3.1 check for intersection between ball and bounding box of drone
 3.2 check for ball direction change (maybe)
 4. return true or false for hit

Pseudocode:

drone_detector = drone_detector.init
ball_detector = ball_detector.init
video = cv2.VideoCapture(args['video'])

for frame in video:
    hit = false
    overlap = false
    drone_boxes = drone_detector(frame)
    for b in drone_boxes:
        (x, y, w, h) = (b.left(), b.top(), b.right(), b.bottom())
        cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)

    ball_centers = ball_detector(frame)
    for c in ball_centers:
        cv2.circle(c)

    if overlap(drone_boxes, ball_centers):
        overlap = true
    
    # create check for direction change (compare 3 frames?)

    if overlap and direction_change:
        hit = true
"""

import cv2
import numpy as np
import imutils
import argparse
import time
from helpers.ball_tracker import ball_tracker

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
args = vars(ap.parse_args())

# grab video from supplied argument
vid = cv2.VideoCapture(args["video"])
time.sleep(2.0)

while True:
    # read the current frame, skip over missing frames
    (grabbed, frame) = vid.read()
    if frame is None:
        continue

    # TODO: detect drone and make frame a smaller local reference around the drone 
    # to eliminate noise from other balls

    # update our frame so it is tracking the ball being shot
    frame = ball_tracker(frame)


    # show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

    # TODO: checking for overlap isn't great because one object would obstruct the other and
    # make object detection tricky. Perhaps check for proximity of ball to drone and a direction
    # change within a few frames of close proximity?

    



    