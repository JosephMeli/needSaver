from simplecrypt import encrypt, decrypt
from os.path import exists
from os import unlink

#TODO delete original user file when encrypted data file created
#TODO add username to the .yaml file title for orginization -> take in extra parameter with jecrpyt and jdecrypt for name


#takes all data from a file and and returns the file as a string
def getText(FILE):
    with open(FILE, 'rb') as myfile:
        data = myfile.read().replace('\n', '')
    return data

#takes a File and encrpyts a string message of that file and loads it into a secret.txt file
def jecrypt(FILE,password):
    myVar = getText(FILE)
    s_Msg =  encrypt(password,myVar)
    #s_Msg.encode('utf8')
    with open('secret.txt','wb') as myfile:
        myfile.write(s_Msg)
    print(s_Msg)

#Takes a secret.txt and decodes message and then writes the decode message to yaml file
def jdecrypt(FILE,password):
    myVar = getText("secret.txt")
    english_Msg = decrypt(password,myVar)
    english_Msg.encode('utf8')
    with open(FILE, 'wb') as myfile:
        myfile.write(english_Msg)
    print(english_Msg)

#TODO fix call for password when you call functions indivdually instead of in a pair
def test_encrpyt_decrypt(FILE,password,):
    jecrypt(FILE,password)
    jdecrypt(FILE,password)