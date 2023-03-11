"""
setup.py is a python file, the presence of which is an indication that the module/package you are about to install has likely been packaged and distributed with Distutils, which is the standard for distributing Python Modules.

This allows you to easily install Python packages. Often it's enough to write:

$ pip install . 
pip will use setup.py to install your module. Avoid calling setup.py directly.

https://docs.python.org/3/installing/index.html#installing-index
https://www.educative.io/answers/what-is-setuppy

"""


from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Dhruv',
author_email='dhruv_agg@protonmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)