'''
The setup.py file is an essential part of packaging and distributing Python projects. 
It is used by setuptools (or distutils in older Python versions) to define the configuration of your project, 
such as its metadata, dependencies, version and more.

'''

from setuptools import find_packages, setup
from typing import List


def get_requirements():
    """

    This function will return list of requirements
    
    """
    requirements_list:List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            #Read Lines
            lines = file.readlines()

            ## Process Each Line:

            for line in lines:
                requirements = line.strip()
                # Ignore empty line and -e.

                if requirements and requirements!="-e .":
                    requirements_list.append(requirements)

    except FileNotFoundError:
        print("requirements.txt file not found!")

    return requirements_list

setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author="Arockia Anand Raj",
    author_email="aroanand3@gmail.com",
    packages=find_packages(),
    requires=get_requirements()

)