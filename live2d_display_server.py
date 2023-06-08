import json

from flask import Flask, send_from_directory, request


app = Flask(__name__, static_folder='dist')

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/assets/<path:path>')
def serve_static(path):
    return send_from_directory('./dist/assets', path)


@app.route('/api/get_mouth_y')
def api_get_one_account():
    with open("tmp.txt", "r") as f:
        return json.dumps({
            "y": f.read()
        })


if __name__ == '__main__':
    app.run(port=4800, debug=True, host="0.0.0.0")