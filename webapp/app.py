from flask import Flask, jsonify, render_template, request, abort
from flask_restful import Resource, Api

import RPi.GPIO as GPIO

# GPIO Config
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

class Led(Resource):
    def get(self, pin_number):
        return jsonify(status=GPIO.input(pin_number))

    def put(self, pin_number):
        if request.form['value'] == "high":
            GPIO.output(pin_number,GPIO.HIGH)
        elif request.form['value'] == "low":
            GPIO.output(pin_number,GPIO.LOW)
        else:
            abort(400)
            
        return jsonify(status=GPIO.input(pin_number))

api.add_resource(Led, '/led/<int:pin_number>')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')