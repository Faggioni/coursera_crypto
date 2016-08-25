import crypto as s
from Crypto.Hash import SHA256 as sha
"""
Test:
03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8
"""
#OJO HEX DECODE
messages = s.split_file('test.mp4',1024)
h=[]
n = len(messages)
ht = sha.new()
for i in range(len(messages)):
    if ((n-i) == n):
       ht.update(messages[n-1])
       h.append(ht.digest())
    else:
        ht.update(messages[n-i-1]+h[i-1])
        h.append(ht.digest())
print len(h)
print h[len(h)-1].encode('hex')
