from flask import Flask
app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'DELETE', 'OPTIONS', 'PUT'])
@app.route('/<path:path>', methods=['GET', 'POST', 'DELETE', 'OPTIONS', 'PUT'])
def hello(path):
    return ""

if __name__ == '__main__':
    app.run("0.0.0.0", port=8080)
