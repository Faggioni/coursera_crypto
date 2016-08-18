"""
  @author: Miguel Faggioni
"""
"""
Functions Used in the Project
"""

from Crypto.Cipher import AES as aes
from Crypto import Random as r

"""
USE     STR ='ASSFACE'
PRINT STR[0:2] -> ASS
"""

#Separate IV and CT from whole CT
def separate_ct(ct_input):
    iv = ct_input[0:16]
    ct = ct_input[16:]
    return iv,ct

#Separate K1 and K from K
def separate_keys(key):
    k1 = key[0:16]
    k = key[16:]
    return k1,k

#Decrypt Function
def decrypt_block_CTC(key, iv, ct):
    print ct
    print ct.decode('hex')
    print iv.decode('hex')
    ct = ct.decode('hex')
    m = aes.new(key.decode('hex'),aes.MODE_CBC,iv)
    ciphertext = format_ct(ct)
    return m.decrypt(ciphertext)

# xor two strings of different lengths
def strxor(a, b):
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def tobinary(str):
   #return ''.join(format(ord(x), 'b') for x in str)
    return ''.join(format(x,'b') for x in bytearray(str))

# Example of Encription - Post in the Documentation
def runtest():
    key = b'Sixteen byte key'
    print key
    print type(key)
    iv = r.new().read(aes.block_size)
    print iv
    print type(iv)
    cipher = aes.new(key, aes.MODE_CFB, iv)
    print cipher
    print type(cipher)
    print iv + cipher.encrypt(b'Attack at dawn')
    print type(iv + cipher.encrypt(b'Attack at dawn'))

#Format ct in blocks of 16 bytes
def format_ct(str):
    while (len(str) % 16 != 0):
        str += 'X'
    return str

