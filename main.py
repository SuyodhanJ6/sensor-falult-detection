# from sensor.configuration.mongo_db_connection import MongoDBClient

# if __name__ == '__main__':
#     mongodb_client = MongoDBClient()
#     print("collection name : ",mongodb_client.database.list_collection_names()) 

from sensor.exception import SensorException
from sensor.logger import logging
import os , sys
from sensor.pipline.training_pipeline import TrainPipeline
# from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionPipeConfig


if __name__ == '__main__':
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
    # training_pipeline_config = TrainingPipelineConfig()
    # data_ingestion_dir = DataIngestionPipeConfig(training_pipeline_config=training_pipeline_config)
    # print(data_ingestion_dir.__dict__)