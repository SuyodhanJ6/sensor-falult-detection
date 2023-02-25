import os, sys
import yaml
from sensor.exception import SensorException


def read_yml_file(file_path : str) -> dict:
    """
    Method Name: read_yml_file
    Description: We are reading yaml file.
    Output     : yaml file
    OnFailure  : Raise exception
    """
    
    with open(file_path, 'r') as yaml_file:
        try:
            return yaml.safe_load(yaml_file)
        except Exception as e:
            raise SensorException(e, sys)

def write_yml_file(file_path : str, content : object, replace : bool = False) -> None:
    """
    Method Name: write_yml_file
    Description: This method help to write a yaml file if it exists then its create new file and replace to first file.
    Output     : yaml file
    OnFailure  : Raise exception
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
            
    except Exception as e:
        raise SensorException(e, sys)
    