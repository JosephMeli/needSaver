# Copyright Joseph Meli (2017)
import os
from user import *
from jyaml import *

#TODO verity that there is a user file -> if not create one
#TODO look into encrypting the user file
FILE="user.yaml"
SALARY=0.00
WEEKS = 0
TAX = 0.0
#User Object to grab from yaml config files
joe = User("Joe",31200,15,52)
joe.displayUser()


if __name__ == '__main__':
    jbegin(FILE)