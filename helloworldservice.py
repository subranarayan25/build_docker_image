from flask import Flask
import json
import os
import socket

app = Flask("helloworldservice")

@app.route('/')
def hello():
    message={
     'message': "HelloWorld",
     'server': socket.gethostname()
    }
    return json.dumps(message, indent=2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)