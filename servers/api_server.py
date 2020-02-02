from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('/home/kagan/Documents/python/Raspberry_pi_iot/servers/test.json', 'r') as output:
    data = json.load(output)


@app.route('/rooms')
def get_rooms():
    keys = list(dict.keys(data['rooms']))
    return jsonify({'rooms': keys})


@app.route('/rooms/<string:room>')
def get_room(room):
    return jsonify({room: data['rooms'][room]})


@app.route('/rooms/<string:room>/<string:prop_of_room>')
def get_lights_by_room(room, prop_of_room):
    return jsonify({room: {prop_of_room: data['rooms'][room][prop_of_room] }})


@app.route('/rooms/<string:room>/<string:prop_of_room>/<string:prop_name>')
def get_ligth_by_name(room, prop_of_room, prop_name):
    return jsonify({room: {prop_of_room: {prop_name: data['rooms'][room][prop_of_room][prop_name] }}})


if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')
