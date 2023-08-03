from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This function will return the list of requirements    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements.txt]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Bharath Raj',
    author_email='gbharath.g80@gmail.com',
    packages=find_packages(),  #find __init__.py and build the packages
    install_requires=get_requirements('requirements.txt')


)