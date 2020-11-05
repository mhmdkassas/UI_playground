from flask import Flask, render_template, Response, request, redirect, url_for, stream_with_context, make_response
from threading import Thread
import random
import os
import cv2
from PIL import Image
from matplotlib import cm
import numpy as np
import time
from datetime import datetime
from random import randint

class Draft3:
    def __init__(self):
        #there 15 variables + self
        self.init_web_server()


    def init_web_server(self):
        template_dir = os.path.dirname(os.path.realpath(__file__))
        template_dir = os.path.join(template_dir,'templates')
        print(template_dir)

        app = Flask(__name__, template_folder=template_dir)

        @app.route("/")
        def index():
            return render_template('home.html')

        @app.route("/home_page", methods=['GET', 'POST'])
        def home_page():
            return render_template('home.html')

        @app.route('/robot_status/', methods = ['GET', 'POST'])
        def nav_status():
            return render_template("robot_status.html")
        
        @app.route('/robot_interaction/', methods = ['GET', 'POST'])
        def nav_interaction():
            return render_template("robot_interaction.html")

        @app.route('/arm/', methods = ['GET', 'POST'])
        def nav_arm():
            return render_template("arm.html")

        @app.route('/video_stream/', methods = ['GET', 'POST'])
        def nav_video():
            return render_template("video_stream.html")

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

        @app.route('/gpio1_feed')
        def  gpio1_feed():
            def gen_gpio1():
                yield str(randint(0, 10))
            return Response(gen_gpio1(), mimetype='text')

        @app.route('/gpio2_feed')
        def  gpio2_feed():
            def gen_gpio2():
                yield str(randint(0, 10))
            return Response(gen_gpio2(), mimetype='text')

        @app.route('/sonar_feed')
        def  sonar_feed():
            def gen_sonar():
                yield str(randint(0, 10))
            return Response(gen_sonar(), mimetype='text')

        @app.route('/infrared_feed')
        def  infrared_feed():
            def gen_infrared():
                yield str(randint(0, 10))
            return Response(gen_infrared(), mimetype='text')

        @app.route('/encoders_feed')
        def  encoders_feed():
            def gen_encoders():
                yield str(randint(0, 10))
            return Response(gen_encoders(), mimetype='text')

        @app.route('/jointx_feed')
        def  jointx_feed():
            def gen_jointx():
                yield str(randint(0, 10))
            return Response(gen_jointx(), mimetype='text')

        @app.route('/jointy_feed')
        def  jointy_feed():
            def gen_jointy():
                yield str(randint(0, 10))
            return Response(gen_jointy(), mimetype='text')

        @app.route('/jointz_feed')
        def  jointz_feed():
            def gen_jointz():
                yield str(randint(0, 10))
            return Response(gen_jointz(), mimetype='text')

        @app.route('/us1_feed')
        def  us1_feed():
            def gen_us1():
                yield str(randint(0, 10))
            return Response(gen_us1(), mimetype='text')

        @app.route('/us2_feed')
        def  us2_feed():
            def gen_us2():
                yield str(randint(0, 10))
            return Response(gen_us2(), mimetype='text')

        @app.route('/us3_feed')
        def  us3_feed():
            def gen_us3():
                yield str(randint(0, 10))
            return Response(gen_us3(), mimetype='text')

        @app.route('/us4_feed')
        def  us4_feed():
            def gen_us4():
                yield str(randint(0, 10))
            return Response(gen_us4(), mimetype='text')

        @app.route('/left_feed')
        def  left_feed():
            def gen_left():
                yield str(randint(0, 10))
            return Response(gen_left(), mimetype='text')

        @app.route('/center_feed')
        def  center_feed():
            def gen_center():
                yield str(randint(0, 10))
            return Response(gen_center(), mimetype='text')

        @app.route('/right_feed')
        def  right_feed():
            def gen_right():
                yield str(randint(0, 10))
            return Response(gen_right(), mimetype='text')

        @app.route('/move_xy/', methods = ['GET', 'POST'])
        def move_xy():
            x = request.form["num_x"]
            y = request.form["num_y"]
            print("x: " + x)
            print("y: " + y)

            return render_template("robot_interaction.html")

        @app.route("/home_coord/", methods = ['GET', 'POST'])
        def home_coord():
            x = request.form["home_x"]
            y = request.form["home_y"]
            z = request.form["home_z"]

            print("x: " + x)
            print("y: " + y)
            print("z: " + z)

            return render_template("robot_interaction.html")

        @app.route("/arm_cont/", methods=['GET', 'POST'])
        def arm_cont():
            j1 = request.form["joint1"] 
            j2 = request.form["joint2"]
            j3 = request.form["joint3"]
            j4 = request.form["joint4"]

            print("j1: " + j1)
            print("j2: " + j2)
            print("j3: " + j3)
            print("j4: " + j4)

            return render_template("arm.html")

        
        app.run()

if __name__ == '__main__':
    draft3 = Draft3()