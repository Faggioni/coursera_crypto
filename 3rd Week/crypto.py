from Crypto.Hash import SHA256 as sha
import os

h = sha.new()
h.update('hello')
print h.hexdigest


statinfo = os.stat('6.2.birthday.mp4')
f = open('test.mp4','r')
print statinfo.st_size / 1024.0
print f
f.close()
