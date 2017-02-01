from simplecrypt import encrypt, decrypt
from os.path import exists
from os import unlink

#take in a string and then turn -> delete file -> creat secret.txt with yaml encryted string ->
# then decrypt string -> create a user.yaml -> yaml.load decrypted string into file ... then load into a user.yaml
def getText(FILE):
    with open(FILE, 'rw') as myfile:
        data = myfile.read().replace('\n', '')
    return data
def writeText(FILE,stringVal):
    


def jdcrypt():

def jcrypt(password,stringVal):
    ciphertext = encrypt(password,stringVal)
    return ciphertext

def read_encrypted(password, filename, string=True):
    with open(filename, 'rb') as input:
        ciphertext = input.read()
        plaintext = decrypt(password, ciphertext)
        if string:
            input.write(plaintext)
            return plaintext.decode('utf8')
        else:
            input.write(plaintext)
            return plaintext

def write_encrypted(password, filename, plaintext):
    with open(filename, 'wb') as output:
        ciphertext = encrypt(password, plaintext)
        ciphertext.encode('utf8')
        output.write(ciphertext)
