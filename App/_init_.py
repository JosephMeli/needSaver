import yaml
import os
# Copyright Joseph Meli (2017)
#TODO verity that there is a user file -> if not create one
#TODO look into encrypting the user file
#User Object to grab from yaml config files
class User:
    def __init__(self, name, salary, weeks):
        self.name = name
        self.salary = salary
        self.weeks = weeks
    def __repr__(self):
         return "%s(name=%r, salary=%r, weeks=%r)" % (
             self.__class__.__name__, self.name, self.salary, self.weeks)
data = """
name: Joseph Meli
salary: 31,200
weeks: 52
"""
stream = open('user.yaml', 'w')
yaml.dump(data, stream)
print (yaml.dump(data))