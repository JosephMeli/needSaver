from simplecrypt import encrypt, decrypt
import os
#TODO delete original user file when encrypted data file created
#TODO add username to the .yaml file title for orginization -> take in extra parameter with jecrpyt and jdecrypt for name


#takes all data from a file and and returns the file as a string
def getText(FILE):
    with open(FILE, 'rb') as myfile:
        data = myfile.read().replace('\n', '')
    return data

#takes a File and encrpyts a string message of that file and loads it into a secret.txt file
def jecrypt(message,password):
    s_Msg =  encrypt(password,message)
    #s_Msg.encode('utf8')
    # with open('secret.txt','wb') as myfile:
    #     myfile.write(s_Msg)
    print("Encrypted Message: " + s_Msg)
    return s_Msg

#Takes a secret.txt and decodes message and then writes the decode message to yaml file
def jdecrypt(message,password):
    english_Msg = decrypt(password,message)
    english_Msg.encode('utf8')
    # with open(FILE, 'wb') as myfile:
    #     myfile.write(english_Msg)
    print("Decrypted Message: " + english_Msg)
    return english_Msg

#TODO fix call for password when you call functions indivdually instead of in a pair
def test_encrpyt_decrypt(FILE,password,):
    jecrypt(FILE,password)
    jdecrypt(FILE,password)


#Takes in the Username and password
#decrypts base on thos attributes
#restores the username.yaml for app use
#deletes secret.text
def load_start(username,password):
    myVar =  getText(username+'.text')
    english = jdecrypt(myVar,password)
    with open(username+'yaml','w') as myfile:
        myfile.write(english)
    os.remove(username + '.text')

#Takes in the Username and password
#encrypts based on thos attributes
#restores the secret.tex for securing information
#delete username.yaml
def save_finish(username,password):
    myVar =  getText(username+'.yaml')
    secret = jecrypt(myVar,password)
    with open(username+'text','w') as myfile:
        myfile.write(secret)
    os.remove(username + '.yaml')
