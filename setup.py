from setuptools import find_packages,setup
from typing import List

const = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [
            req.replace("\n"," ") for req in requirements
        ]
        if const in requirements:
            requirements.remove(const)
    return requirements


setup(
    name='Generic ML Project',
    version='0.0.1',
    author='Chandan',
    author_email='csengupta1101@hotmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)