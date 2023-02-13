from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.component.data_ingestion import DataIngestion
from sensor.logger import logging
import os, sys
from sensor.exception import SensorException

class TrainPipeline:
    def __init__(self):
        training_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        self.training_pipeline = training_pipeline_config
        
    def start_data_ingestion(self)->DataIngestionArtifact:
        """
        Method_Name: start_data_ingestion
        Description: This method help to start data ingestion pipeline
        OutPut     : None
        OnFailure  : Raise an exception
        """
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )

            logging.info("Getting the data from mongodb")

            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"completed the data ingestion and artifacts : {data_ingestion_artifact}")   
            return data_ingestion_artifact
            pass
        except Exception as e:
            raise SensorException(e, sys)
        
    def start_data_validation(self):
        try:
            pass
        except Exception as e: 
            raise SensorException(e, sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e: 
            raise SensorException(e, sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e: 
            raise SensorException(e, sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e: 
            raise SensorException(e, sys)
        
    def run_pipeline(self):
        """
        Method_Name: run_pipeline
        Description: This method is first step to data ingestion process
        OutPut     : None
        OnFailure  : Raise an exception
        """
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e: 
            raise SensorException(e, sys)
        