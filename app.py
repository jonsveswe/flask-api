from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'
#     return jsonify({'name':'Jimit',
#                     'address':'India'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')