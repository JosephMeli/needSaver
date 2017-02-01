import yaml, os,warnings
from Crypto.Cipher import AES
def jfile(filename):
    stream = open(filename, 'r')
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
             print(exc)
