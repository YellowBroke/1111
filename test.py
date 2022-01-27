from Crypto.Cipher import AES
from base64 import b64encode
import requests
import random
import json
import os

def to_16(data):
    len1=16-len(data)%16
    data+=chr(len1)*len1

    return data

def encryption(data,key):
    iv = '0102030405060708'
    aes = AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
    data1 = to_16(data)
    bs=aes.encrypt(data1.encode('utf-8'))

    return str(b64encode(bs),'utf-8')

def get_enc(data):
    param4 = '0CoJUm6Qyw8W8jud'
    #enc='NA5SxhePf6dxIxX7'
    #enc='GLvjERPvSFUw6EVQ'
    enc='g4PXsCuqYE6icH3R'
    first=encryption(data,param4)
    return encryption(first,enc)