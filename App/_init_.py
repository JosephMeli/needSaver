# Copyright Joseph Meli (2017)
import os
from user import *
from jyaml import *
from jsecret import *

#TODO verity that there is a user file -> if not create one
#TODO look into encrypting the user file

#GLOBAL variables for later
FILE="user.yaml"
SALARY=0.00
WEEKS = 0
TAX = 0.0

PASSWORD = "secret"
FILENAME = "user.yaml"
DATA='''
name: Josep Meli
Salary: 31200
Tax: 15
Weeks: 52
'''

if __name__ == '__main__':
    #Test for jsceret functions
    save_finish('',PASSWORD)
