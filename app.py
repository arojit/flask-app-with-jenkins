from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "Hello World"
    request_data = request.get_json()


@app.route('/get-message', methods=['POST'])
def message():
    request_data = request.get_json()
    name = request_data['name']
    return jsonify({'message': 'Hello ' + name + ' Welcome!'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
