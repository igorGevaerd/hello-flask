from flask import Flask
app = Flask(__name__)
import socket
name = socket.gethostname()

@app.route('/')
def hello_world():
    return 'Hello, World! <br><br><br> From: %s' % name

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
