# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:50:33 2019

@author: Lucifer
"""

# encrypt and decrypt a text using a simple algorithm of offsetting the letters

key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

text = input("enter the message")
offset = 5

encrypted = encrypt(offset, text)
print('Encrypted:', encrypted)

decrypted = decrypt(offset, encrypted)
print('Decrypted:', decrypted)

'''OUTPUT:
    enter the messagehello Ranjeet
Encrypted: mjqqt wfsojjy
Decrypted: hello ranjeet
    '''