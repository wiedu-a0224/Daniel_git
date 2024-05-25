# app.py
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/drawstick', methods=['POST'])
def run_drawstick():
    result = subprocess.run(['python', 'drawstick.py'], stdout=subprocess.PIPE)
    return jsonify({'result': result.stdout.decode('utf-8')})

if __name__ == '__main__':
    app.run(port=5500)