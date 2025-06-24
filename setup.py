from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file :str)-> List[str]:
    """This function returns the names of required packages and libraries

    Args:
        file (str): Input the name of the requirements.txt file
    """
    requirements = []
    with open(file) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
    

setup(
    name="mlproject",
    version="0.0.1",
    author="Palnika",
    author_email="parnnnikachavan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  
)