# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:13:58 2019

@author: Lucifer
"""

message = 'FLEPYRMWRFYRXCR' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
            if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                        translated = translated + LETTERS[num]
            else:
                translated+=symbol
    print('Resultant key: #%s: %s' % (key, translated))