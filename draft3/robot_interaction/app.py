from flask import Flask, render_template, Response, request, redirect, url_for
from threading import Thread
import random
import os
class Draft3:
    def __init__(self):
        self.init_web_server(0, 0, 0)


    def init_web_server(self, n1, n2, n3):
        template_dir = os.path.dirname(os.path.realpath(__file__))
        template_dir = os.path.join(template_dir,'web')
        print(template_dir)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

        app = Flask(__name__, template_folder=template_dir)
        
        @app.route("/")
        def index():
            return render_template('index.html')

        @app.route("/move_xy/", methods=['GET', 'POST'])
        def move_xy():
            x = request.form["move_x"]
            y = request.form["move_y"]
            print("x: " + x)
            print("y: " + y)
            return render_template("index.html")

        @app.route("/arm_cont/", methods=['GET', 'POST'])
        def control_arm():
            joint1 = request.form["joint1"]
            joint2 = request.form["joint2"]
            joint3 = request.form["joint3"]
            joint4 = request.form["joint4"]

            print("joint1" + joint1)
            print("joint2" + joint2)
            print("joint3" + joint3)
            print("joint4" + joint4)

            return render_template("index.html")
        
        @app.route("/home/", methods=['GET', 'POST'])
        def home_coord():
            x = request.form["home_x"]
            y = request.form["home_y"]
            z = request.form["home_z"]

            print("x: " + x)
            print("y: " + y)
            print("z: " + z)

            return render_template("index.html")
            
        app.run()

if __name__ == '__main__':
    draft3 = Draft3()