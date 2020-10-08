from flask import Flask, render_template, Response, request, redirect, url_for
from threading import Thread
import random
import os
import cv2
class Draft3:
    def __init__(self):
        self.init_web_server(0, 0, 0, 0, 0, 0)


    def init_web_server(self, ultrasonic, infrared, encoders, jointx1, jointx2, jointx3):
        template_dir = os.path.dirname(os.path.realpath(__file__))
        template_dir = os.path.join(template_dir,'web')
        print(template_dir)
        self.ultrasonic = ultrasonic
        self.infrared = infrared
        self.encoders = encoders
        self.jointx1 = jointx1
        self.jointx2 = jointx2
        self.jointx3 = jointx3

        app = Flask(__name__, template_folder=template_dir)
        
        @app.route("/")
        def index():
            return render_template('index.html')

        @app.route("/move_xy/", methods=['GET', 'POST'])
        def move_xy():
            x = request.form["num_x"]
            y = request.form["num_y"]
            print("x: " + x)
            print("y: " + y)
            return render_template("index.html", ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3)

        
        @app.route("/home/", methods=['GET', 'POST'])
        def home_coord():
            x = request.form["home_x"]
            y = request.form["home_y"]
            z = request.form["home_z"]

            print("x: " + x)
            print("y: " + y)
            print("z: " + z)

            return render_template("index.html", ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3)

        @app.route("/ultrasonic/", methods=['GET', 'POST'])
        def ultrasonic_finder():
            self.ultrasonic= random.randint(100, 150)
            return render_template('index.html', ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3)

        @app.route("/infrared/", methods=['GET', 'POST'])
        def infrared_finder():
            self.infrared= random.randint(100, 150)
            return render_template('index.html', ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3)

        @app.route("/encoders/", methods=['GET', 'POST'])
        def encoders_finder():
            self.encoders = random.randint(100, 150)
            return render_template('index.html', ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3)

        @app.route("/jointx/", methods=['GET', 'POST'])
        def jointx1_finder():
            self.jointx1= random.randint(100, 150)
            return render_template('index.html', ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3)

        @app.route("/jointy/", methods=['GET', 'POST'])
        def jointx2_finder():
            self.jointx2= random.randint(100, 150)
            return render_template('index.html', ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3)

        @app.route("/jointz/", methods=['GET', 'POST'])
        def jointx3_finder():
            self.jointx3= random.randint(100, 150)
            return render_template('index.html', ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3)

            
        app.run()

if __name__ == '__main__':
    draft3 = Draft3()