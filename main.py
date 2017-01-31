import yaml,os,stat
# Copyright Joseph Meli (2017
filename = 'user.yaml'
mode = 0600|stat.S_IRUSR
try:
    os.open('user.yaml', 'rw')
except:
    os.mknod(filename,mode)
    print('created user file')
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
stream = file('user.yaml', 'w')
yaml.dump(data, stream)
print yaml.dump(data)