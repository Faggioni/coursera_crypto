"""
Created by Faggioni
Python Script
@author: Miguel Faggioni

"""

import sys

#MSGS = ( ---  11 secret messages  --- )

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]

def only_letters(a):
    w_a = ''
    for x in a:
        if 65<= ord(x) and ord(x) <= 90:
            w_a += x
        elif 97<= ord(x) and ord(x) <= 122:
            w_a += x
        else:
            w_a += ' '
    print w_a

def test_keys(cyphers,messages):
    keys = []
    for x in cyphers:
        for y in messages:
            keys.append(strxor(x,y))

    final_key=''
    for x in keys:
        for letters in x:
            if 65<= ord(x) and ord(x) <= 90:
                final_key += x
            elif 97<= ord(x) and ord(x) <= 122:
                final_key += x
            else:
                final_key += ' '

def test_key(cypher,message):

    key = strxor(cypher,message)
    final_key=''

    for x in key:
        if 65<= ord(x) and ord(x) <= 90:
            final_key += x
        elif 97<= ord(x) and ord(x) <= 122:
            final_key += x
        else:
            final_key += ' '

    print final_key




