# Main GUI
The [gui_server](/gui_server/) folder is what the base station would use to receive the live streaming video data from the Raspberry Pi and send commands through a simple interface.

![](/imgs/gui_demo.png)



Although the UI functionality of the left side currently doesn't work, the plan is to connect them to interface with the UAV's parts. As well as display informational data coming from the drone's hardware.

# Functionality of vidServer.py
VidServer creates a server in a thread constantly waiting for a client to connect. Once a connection has been made, it will decode the message using NumPy and add it to the Queue as a buffer.

To get the image, calling getImg() will get one frame at a time. If there are no more recent frames, it will return None, and if elapsedWaitTime passes 3 seconds, it will return a static image to prevent the window from crashing.

```python
def getImg(self):
        # Image from client
        elapsedWaitTime = time.time() - self.startTime
        if not self.que.empty():
            self.startTime = time.time()
            item = self.que.get()
            self.recent_message = item
            return item
        # Stock image to prevent the crash of lack of data
        elif elapsedWaitTime > 3:
            image = cv2.imread('disconnected.png')
            return image
        return None
```

# Functionality of vidClient.py

This example of running vidClient.py will forever stream video data while running another task.
```python
if __name__ == "__main__":
    print("Starting client")
    sendVideo = vidClient("10.000.000.00", 6789) # Server IP address and port
    while True:
        print("Running background Task")
        time.sleep(1)
```

Note in the vidClient.py file to use a webcam in windows you would have to use
```python
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```
In linux you would remove cv2.CAP_DSHOW

# Future GUI Implementation
The GUI was built to first stream the video data, but there are functions built where a button is clicked, it will call a function using slots and signals. Future implementation would be connecting functionality with the buttons to move the servos. update_info() would constantly receive info from the UAV and update the fields as another method to monitor the status of the drone.