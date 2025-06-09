'''
The setup.py file is an essential part of packaging and distributing Python projects. 
It is used by setuptools (or distutils in older Python versions) to define the configuration of your project, 
such as its metadata, dependencies, version and more.

'''

from setuptools import find_packages, setup     
'''findpackages- function all the folders and whenever the file contain __init__.py then it is considered as a package'''
from typing import List




def get_requirements()-> List[str]:
    """
        --> This function will return list of requirements
    """

    requirement_list:List[str] = []

    try:
        with open("requirements.txt") as f:
            # Read lines from the f
            lines = f.readlines()

            # Process each line:
            for line in lines:
                ### Remove white space
                requirement = line.strip()

                ###ignore emplty lines and -e .
                if requirement and requirement !='-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("No requirements.txt file found")

    return requirement_list


## Setup our meta data:

setup(
    name= "NetworkSecurity",
    version="1.0",
    author="Anand",
    author_email="aroanand3@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)