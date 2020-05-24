import random
import socket
from flask import Flask
from math import gcd
from time import time

app = Flask(__name__)

@app.route('/')
def root():
    host_name = socket.gethostname()
    return f'OK (server: {host_name})'

@app.route('/expensive')
def expensive():
    num1 = random.randint(1, 5)
    # until = time() + num1
    until = time() + 15
    while time() < until:1
    return 'Waiting done'
    # num1 = random.randint(100000000000000, 10000000000000000)
    # num2 = random.randint(100000000000000, 10000000000000000)
    # res = gcd(num1, num2)

    # return f'GCD of {num1} and {num2}: {res}'


def is_prime(n):
   if n <= 1 or n % 1 > 0:
      return False
   for i in range(2, n//2):
      if n % i == 0:
         return False
   return True