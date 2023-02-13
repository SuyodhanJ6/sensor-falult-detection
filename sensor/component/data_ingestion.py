from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.data_access.sensor_data import SensorData
import sys, os
from pandas import DataFrame
from sklearn.model_selection import train_test_split

class DataIngestion:
    
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)
        
    def export_data_into_feature_store(self)->DataFrame:
        """
        Method Name : export_data_into_feature_store
        Description : This method help to data export Mongo DB collection to data frame. 
        Output      : DataFrame
        OnFailure   : Raise exception
        """
        try:
            logging.info("Export data from MongoDB to feature store")
            sensor_data = SensorData()
            dataframe = sensor_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name)

            # Creating a Folder 
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            # Converting dataframe to csv file 
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            
        except Exception as e:
            raise SensorException(e, sys)
        
    def split_data_train_test(self, dataframe: DataFrame):
        """_
        Method Name : split_data_train_test
        Description : Feature Store dataset will split into train and test. 
        Output      : Crating train and test   folder 
        OnFailure   : Raise exception
        """
        logging.info("Entering split_data_train_test method in data_ingestion class.")
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train_test_split on dataframe.")
            
            logging.info("Exited split_data_as_train_test method of Data_ingestion class.")
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info(f"Exploring train and test file path. ")
            
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )            

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )  
        except Exception as e:
            raise SensorException(e, sys)  
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            dataframe = self.export_data_into_feature_store()
            self.split_data_train_test(dataframe=dataframe)
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                  test_file_path=self.data_ingestion_config.testing_file_path)
            
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e, sys)   