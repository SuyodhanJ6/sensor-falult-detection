from setuptools import find_packages, setup
from typing import List

def get_required()->List[str]:
    
    """
    Method Name : 
    Description : This method help to get all the package name.
    OutPut      : str
    OnFailure   : None
    """
    
    
    requirement_list:List[str] = []
    
    return requirement_list

setup(
    name = "sensor",
    version="0.0.1",
    author="Prashant",
    author_email="prashantmalge181@gmail.com",
    packages= find_packages(),
    install_requires = get_required()
)