#!/usr/bin/env python3
from flask import Flask
import time

app = Flask(__name__)
logfile = 'uuid.log'

@app.route("/")
def root():
    return ""

@app.route("/uuid/<path:uuid>")
def uuid(uuid=None):
    with open(logfile, 'a') as f:
        f.write('{},{}'.format(time.time(),uuid))
    return "Thank you!"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
