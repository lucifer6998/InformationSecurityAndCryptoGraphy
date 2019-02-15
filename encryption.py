# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:08:50 2019

@author: Lucifer
"""

cypherText=""
rawText = input("enter the message")
key =int(input("enter key value 1~9"))
for i in range(len(rawText)):
    c=rawText[i]
    if(c.isupper()):
        cypherText+= chr((ord(c)+ key-65)%26 +65)
        
    else:
         cypherText += chr((ord(c) + key-97) % 26 + 97)
    cypherText=cypherText.upper()

print(cypherText)