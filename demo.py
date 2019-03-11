#!/usr/bin/python

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    # Camera warm-up time
    time.sleep(2)
    camera.start_recording('/data/video.h264')
    sleep(10)
    camera.stop_recording()
