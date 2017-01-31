# Copyright Joseph Meli (2017)
import yaml
import os
from core import *

#TODO verity that there is a user file -> if not create one
#TODO look into encrypting the user file
#User Object to grab from yaml config files

joe = User("Joe",31200,52)
joe.displayUser()


if __name__ == '__main__':
    data = """
    name: Joseph Meli
    salary: 31,200
    weeks: 52
    """
    stream = open('user.yaml', 'w')
    yaml.dump(data, stream)
    print(yaml.dump(data))