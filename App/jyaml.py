import yaml, os,warnings

def jfile(filename):
    stream = open(filename, 'r')
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
             print(exc)

