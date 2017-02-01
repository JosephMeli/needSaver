# Copyright Joseph Meli (2017)
import os
from user import *
from jyaml import *
from secret import *

#TODO verity that there is a user file -> if not create one
#TODO look into encrypting the user file
FILE="user.yaml"
SALARY=0.00
WEEKS = 0
TAX = 0.0

PASSWORD = "secret"
FILENAME = "user.yaml"
#User Object to grab from yaml config files
joe = User("Joe",31200,15,52)
joe.displayUser()


DATA="'\nname: Josep Meli\nSalary: 31200\nTax: 15\nWeeks: 52\n'"
if __name__ == '__main__':
    jfile(FILE)
    try:
        write_encrypted(PASSWORD,FILENAME,DATA)
    except:
        read_encrypted(PASSWORD, FILENAME, string=True)
