from djitellopy import Tello

import cv2 as cv

drone = Tello()

drone.connect()
drone.stream_on()
cam = drone.get_frame_read()

while True:
    frame = cam.frame
    cv.imshow("Frame", frame)
    if cv.waitKey(0) & 0xFF == ord("q"):
        break
drone.streamoff()
