#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
import threading
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from flask import Flask, render_template, Response

app = Flask(__name__)

class image_converter:

  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/image_raw",Image,self.callback)

  def callback(self,data):

    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print("error")
      print(e)

    (rows,cols,channels) = cv_image.shape

    success, frame = camera.read()  # read the camera frame
    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    yield (b'--frame\r\n'                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def main(args):
  ic = image_converter()
  threading.Thread(target=lambda: rospy.init_node('image_converter', anonymous=True)).start()



if __name__ == '__main__':
    main(sys.argv)
    app.run(host='0.0.0.0', port=4996)
