# AI Generated script to test if the pi cam works
# Dependicies: pip install picamera
#              pip install opencv-python-headless
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

# Initialize the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warm up
time.sleep(0.1)

# Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # Grab the raw NumPy array representing the image
    image = frame.array

    # Display the frame
    cv2.imshow("Frame", image)

    # Clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # Wait for the 'q' key to stop the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cv2.destroyAllWindows()