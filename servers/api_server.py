from flask import Flask, jsonify

app = Flask(__name__)

lights = {'lights':
          {
              'light1': False,
              'light2': False,
              'light3': False
          }
          }


@app.route('/lights')
def get_lights():
    return jsonify(lights)


@app.route('/lights/<string:light>')
def get_ligth(light):
    return jsonify({light: lights['lights'][light]})


@app.route('/lights/<string:light>/on')
def open_ligth(light):
    lights['lights'][light] = True
    return jsonify({light: lights['lights'][light]})


@app.route('/lights/<string:light>/off')
def close_ligth(light):
    lights['lights'][light] = False
    return jsonify({light: lights['lights'][light]})


if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')
