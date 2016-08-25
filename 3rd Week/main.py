import crypto as s
from Crypto.Hash import SHA256 as sha
import sys
"""
Test:
03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8
"""
#OJO HEX DECODE
messages = s.splitting('6.1.intro.mp4',1024)
h=[]
n = len(messages)-1
print sys.getsizeof(messages[0])
for i in range(n+1):
    if ((n-i) == n):
        ht = sha.new()
        ht.update(messages[n])
        h.append(ht.digest())
    else:
        ht = sha.new()
        ht.update(messages[n-i]+h[i-1])
        h.append(ht.digest())
print h[len(h)-1].encode('hex')
