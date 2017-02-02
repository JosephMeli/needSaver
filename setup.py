# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()
#TODO include need install component of setup.py for all packages in requirements.txt
setup(
    name='needSaver',
    version='0.0.0',
    description='Savings and Money Assistant App',
    long_description=readme,
    author='Joseph Meli',
    author_email='joemeli631@gmail.com',
    url='https://github.com/JosephMeli/needSaver',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
