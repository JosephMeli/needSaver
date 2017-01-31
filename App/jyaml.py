import yaml, os,warnings

def jbegin(filename):
    with open(filename, 'r') as stream:
        try:
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)
def jdone(fil)