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

        @app.route("/rand_num1/", methods=['GET', 'POST'])
        def get_rand_num1():
            self.n1 = random.randint(1, 50)
            return render_template('index.html', number1 = self.n1, number2 = self.n2, number3 = self.n3)

        @app.route("/rand_num2/", methods=['GET', 'POST'])
        def get_rand_num2():
            self.n2 = random.randint(50, 100)
            return render_template('index.html',number1 = self.n1, number2 = self.n2, number3 = self.n3)

        @app.route("/rand_num3/", methods=['GET', 'POST'])
        def get_rand_num3():
            self.n3 = random.randint(100, 150)
            return render_template('index.html',number1 = self.n1, number2 = self.n2, number3 = self.n3)   

        app.run()

if __name__ == '__main__':
    draft3 = Draft3()