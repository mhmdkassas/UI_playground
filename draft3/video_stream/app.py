from flask import Flask, render_template, Response, request, redirect, url_for
from threading import Thread
import random
import os
import cv2
from PIL import Image
from matplotlib import cm
import numpy as np
import time

class Draft3:
    def __init__(self):
        self.init_web_server()


    def init_web_server(self,):
        template_dir = os.path.dirname(os.path.realpath(__file__))
        template_dir = os.path.join(template_dir,'web')
        print(template_dir)
        

        app = Flask(__name__, template_folder=template_dir)
        
        @app.route("/")
        def index():
            return render_template('index.html')
        
        def gen():
            vc = cv2.VideoCapture(0)
            while True:
                _, frame = vc.read()
                _, im = cv2.imencode(".jpeg", frame)
                frame = im.tobytes()
                yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        @app.route("/video_feed")
        def video_feed():
            vc = cv2.VideoCapture(0)
            rval, frame = vc.read()
            ret, im = cv2.imencode(".jpeg", frame)
            return Response((gen()), mimetype='multipart/x-mixed-replace; boundary=frame')

        app.run(threaded=True)

if __name__ == '__main__':
    draft3 = Draft3()