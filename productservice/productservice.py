import random
import socket
from flask import Flask
from math import gcd
from time import time

app = Flask(__name__)

@app.route('/')
def root():
    host_name = socket.gethostname()
    return f'OK (server: {host_name})\n'

@app.route('/expensive')
def expensive():
    num1 = random.randint(1, 5)
    until = time() + num1
    # until = time() + 15
    while time() < until:1
    return 'Waiting done\n'

