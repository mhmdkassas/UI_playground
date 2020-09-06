from flask import Flask, render_template, Response, request, redirect, url_for
from threading import Thread
import random
import os
class Draft3:
    def __init__(self):
        #there 15 variables + self
        self.init_web_server(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


    def init_web_server(self, gpio1, gpio2, ultrasonic, infrared, encoders, jointx1, jointx2, jointx3, us1, us2, us3, us4, left, center, right):
        template_dir = os.path.dirname(os.path.realpath(__file__))
        template_dir = os.path.join(template_dir,'web')
        print(template_dir)
        self.gpio1 = gpio1
        self.gpio2 = gpio2
        self.ultrasonic = ultrasonic
        self.infrared = infrared
        self.encoders = encoders
        self.jointx1 = jointx1
        self.jointx2 = jointx2
        self.jointx3 = jointx3
        self.us1 = us1
        self.us2 = us2
        self.us3 = us3
        self.us4 = us4
        self.left = left
        self.center = center
        self.right = right

        app = Flask(__name__, template_folder=template_dir)
        
        @app.route("/")
        def index():
            return render_template('index.html')

        @app.route("/gpio1/", methods=['GET', 'POST'])
        def gpio1_finder():
            self.gpio1 = random.randint(1, 50)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/gpio2/", methods=['GET', 'POST'])
        def gpio2_finder():
            self.gpio2 = random.randint(50, 100)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)
  
        @app.route("/ultrasonic/", methods=['GET', 'POST'])
        def ultrasonic_finder():
            self.ultrasonic= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/infrared/", methods=['GET', 'POST'])
        def infrared_finder():
            self.infrared= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/encoders/", methods=['GET', 'POST'])
        def encoders_finder():
            self.encoders = random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/jointx/", methods=['GET', 'POST'])
        def jointx1_finder():
            self.jointx1= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/jointy/", methods=['GET', 'POST'])
        def jointx2_finder():
            self.jointx2= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/jointz/", methods=['GET', 'POST'])
        def jointx3_finder():
            self.jointx3= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/us1/", methods=['GET', 'POST'])
        def us1_finder():
            self.us1= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/us2/", methods=['GET', 'POST'])
        def us2_finder():
            self.us2= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)
        
        @app.route("/us3/", methods=['GET', 'POST'])
        def us3_finder():
            self.us3= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/us4/", methods=['GET', 'POST'])
        def us4_finder():
            self.us4= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/left/", methods=['GET', 'POST'])
        def left_finder():
            self.left= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/center/", methods=['GET', 'POST'])
        def center_finder():
            self.center= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)

        @app.route("/right/", methods=['GET', 'POST'])
        def right_finder():
            self.right= random.randint(100, 150)
            return render_template('index.html', gpio1=self.gpio1, gpio2=self.gpio2, ultrasonic=self.ultrasonic, infrared=self.infrared, encoders=self.encoders, jointx1 = self.jointx1, jointx2=self.jointx2, jointx3 = self.jointx3, us1 = self.us1, us2 = self.us2, us3 = self.us3, us4 = self.us4, left=self.left, center=self.center, right=self.right)
            
        app.run()

if __name__ == '__main__':
    draft3 = Draft3()