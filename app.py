from flask import Flask
app = Flask(__name__)
import socket
name = socket.gethostname()

@app.route('/')
def hello():
  return "Hello World! \n\n\n From: %s" % name

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
