from flask import Flask, render_template,jsonify
import requests


app = Flask(__name__)


def get_id():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    api = 'http://' + s.getsockname()[0] + ':5001/lights'
    s.close()
    return api


@app.route('/')
def index():
    return 'Hello world'


@app.route('/lights')
def get_lights():
    request_data = requests.get(api)
    json_obj = request_data.json()
    return render_template('index.html', lights=json_obj)

# @app.route('/lights?light1=on')
# def tst():
#     return 'OK'


if __name__ == "__main__":
    api = get_id()
    app.run(debug=True, host='0.0.0.0')
