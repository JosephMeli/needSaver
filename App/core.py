import yaml
import os
class User:
    def __init__(self, name, salary, weeks):
        self.name = name
        self.salary = salary
        self.weeks = weeks
    def displayUser(self):
        print ("Name : ", self.name, ", Salary: ", self.salary,", Weeks: ", self.weeks)
    def getUser(self):
       return (self.name,self.salary,self.weeks)