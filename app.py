from flask import Flask, jsonify, request
from sense_hat import SenseHat
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#cors = CORS(app, resources={r'/*': {'origins': 'http://169.254.207.87'}})# allow this domain to access api
sense = SenseHat()
sense.set_imu_config(True, True, True)  # compass, gyroscope, accel

incomes = [
  { 'description': 'salary', 
    'amount': 5000 }
]

@app.route('/')
def index():
    return 'Hej hej hemma'

@app.route('/orientation', methods=['GET'])
def get_orientation():
    orientation = sense.get_orientation_degrees()
    print(sense.orientation)
    return jsonify(sense.orientation)

@app.route('/incomes')# Default is GET
def get_incomes():
  return jsonify(incomes)
  
@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  print(incomes)
  return '', 204        

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
