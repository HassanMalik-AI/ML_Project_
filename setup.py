from setuptools import find_packages, setup
from typing import List
from src.logger import logging

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements=requirements[:-1]
            
    return requirements

setup(
    name="ML_Project_2",
    version="0.0.1",
    author="Hassan Malik",
    author_email="hassanmalik1437@mail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)