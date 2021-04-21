#!/usr/bin/env python

# Imports
import logging
import subprocess
import sys
from flask import Flask
from threading import Thread

# Initializes the Flask web server.
flask: Flask = Flask('replit_keep_alive')

# Initializes the Logger.
log: logging.Logger = logging.getLogger('werkzeug')

# Method for handling the base route of '/'.
@flask.route('/')
def index() -> str:
    return 'Keeping the repl alive!'

# Wraps the web server run() method in a Thread object and starts the web server.
def keep_alive() -> None:
    def run() -> None:
        log.setLevel(logging.ERROR)
        flask.run(host = '0.0.0.0', port = 8080)
    thread = Thread(target = run)
    thread.start()

# The "main" method essentially. The body of this conditional is executed when this script is
# executed as the main module (ie. not imported by another module)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Error: when executing this script as the main module, you need to pass in the name of the script to keep alive as the first argument. This script may also be imported by another module and used by calling the "keep_alive()" method.', file = sys.stderr)
    else:
        keep_alive()
        subprocess.call(['python', sys.argv[1]])
