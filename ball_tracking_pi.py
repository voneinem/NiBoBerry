# This code is inspired by
# https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
# https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
#
# For the video stream
# https://blog.miguelgrinberg.com/post/video-streaming-with-flask
#
# Goal is to let the NIBOBee follow a green ball - first step is get the deviation from the middle

from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from importlib import import_module
import os
from flask import Flask, render_template, Response
import threading
import io

webFrame = None

def ImageProcessingThread(dummy):
    global webFrame
    # define the lower and upper boundaries of the "green"
    # ball in the HSV color space, then initialize the
    # list of tracked points
    greenLower = (29, 86, 6)
    greenUpper = (64, 255, 255)

    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    
    # allow the camera or video file to warm up
    time.sleep(0.1)

    # capture frames from the camera
    for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
        frame = image.array
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # construct a mask for the color "green", then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

    #	cv2.imshow("mask", mask)

        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
                    # find the largest contour in the mask, then use
                    # it to compute the minimum enclosing circle and
                    # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            print('Object - x = %s \t y = %s\t r = %s' %
                (int(x) - 320, int(y), int(radius)))

            # only proceed if the radius meets a minimum size
            if radius > 5:

                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius),
                            (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

                ret, webFrame = cv2.imencode('.jpg',frame)

            # show the frame to our screen
            #	cv2.imshow("Frame", frame)

        key = cv2.waitKey(1) & 0xFF

        # if the 'q' key is pressed, stop the loop
        if key == ord("q"):
            break

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

imageProcessing = threading.Thread(target = ImageProcessingThread, args= (0.001, ))
imageProcessing.start()
time.sleep(0.1)

## web app ##

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen():
    global webFrame
    """Video streaming generator function."""
    while True:
        frame = webFrame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)