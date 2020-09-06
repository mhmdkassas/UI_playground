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

        app = Flask(__name__, template_folder=template_dir)
        
        @app.route("/")
        def index():
            return render_template('index.html')

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
                    
        app.run()

if __name__ == '__main__':
    draft3 = Draft3()