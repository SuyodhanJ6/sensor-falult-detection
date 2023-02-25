from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from sensor.entity.config_entity import DataValidationConfig
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.utils.main_utils import read_yml_file
    

import os, sys
import pandas as pd

class DataValidation:
    """
    
    """
    def __init__(self,data_ingestion_artifact : DataIngestionArtifact, data_validation_config : DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise SensorException(e, sys)
    
    def valid_number_of_columns(self, dataframe : pd.DataFrame)->bool:
        """
        Method Name : valid_number_of_columns
        Description : Checking the number of columns in the dataframe.
        OutPut      : bool(True/False)
        OnFailure   : raise exception
        """
        try:
            logging.info("Checking the number of columns in the dataframe")
            number_of_columns = len(self._schema_config["columns"])
            if len(dataframe.columns) == number_of_columns:
                return True
            return False
        except Exception as e:
            raise SensorException(e, sys)
        
        
    def is_numerical_column(self, dataframe : pd.DataFrame)->bool:
        try:
            logging.info(" checking is_numerical_column")
            numerical_columns = self._schema_config["numerical_columns"]
            dataframe_columns = dataframe.columns
            
            numerical_columns_present = True
            missing_columns = []
            for num_column in numerical_columns:
                if num_column not in dataframe.columns:
                    numerical_columns_present = False
                    missing_columns.append(num_column)
            logging.info(f"Missing Numerical Column: [{missing_columns}]")
            return numerical_columns_present
        
        except Exception as e:
            raise SensorException(e, sys)
        
    # Assignment
    def drop_zero_std_columns(self, dataframe : pd.DataFrame)->pd.DataFrame:
        try:
            # Calculate the standard deviation of each column
            stds = dataframe.std()
            
            # Find the columns with zero standard deviation
            zero_std_cols = stds[stds == 0].index.tolist()
            
            # Drop the zero standard deviation columns from the DataFrame
            dataframe = dataframe.drop(zero_std_cols, axis=1)
            return dataframe
        except Exception as e:
            raise SensorException(e, sys)
            
    
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        """
        Method Name : read_data
        Description : Reading the csv file form specific location.
        OutPut      : DataFrame
        OnFailure   : raise exception
        """
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise SensorException(e, sys)
        
    
    def detect_datadrift():
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)
        
    def initialize_data_validation(self)->DataValidationArtifact:
        """
        Method Name  : initialize_data_validation
        Description  : All method initialization happens in this method.
        OutPut       : None
        OnFailure    : raise exception
        """
        try:
            error_message = " "
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            # Reading data from train and test files location
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)
            
            ## Validating number of columns
            # Train dataframe 
            status = self.valid_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = f"{error_message} Train Dataframe does not contain all columns "
            # Test dataframe        
            status = self.valid_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message = f"{error_message} Test Dataframe does not contain all columns "
                
            ## Validating Numerical columns
            # Train dataframe
            status = self.is_numerical_column(dataframe=train_dataframe)
            if not status:
                 error_message = f"{error_message} Train Dataframe does not contain all numerical columns "
            # Test dataframe
            if not status:
                error_message = f"{error_message} Test Dataframe does not contain all numerical columns "
                
            # Checking error message length
            if len(error_message) > 0:
                raise Exception(error_message)
            
            # Let's Check data drift 
            
                
        except Exception as e:
            raise SensorException(e, sys)
        


