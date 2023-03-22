import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

from src.components.data_transformation import DataTransformation, DataTransformationConfig

from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

from src.configs.config import DATA_FOLDER, RAW_DATA_FILE_NAME, TEST_SIZE,ARTIFACTS_FOLDER_NAME, TRAIN_DATA_FILE_NAME, TEST_DATA_FILE_NAME, ARTIFACTS_RAW_DATA_FILE_NAME


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join(ARTIFACTS_FOLDER_NAME, TRAIN_DATA_FILE_NAME)
    test_data_path: str = os.path.join(ARTIFACTS_FOLDER_NAME, TEST_DATA_FILE_NAME)
    raw_data_path: str = os.path.join(ARTIFACTS_FOLDER_NAME,ARTIFACTS_RAW_DATA_FILE_NAME )


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            input_file_path = os.path.join(DATA_FOLDER, RAW_DATA_FILE_NAME)
            df = pd.read_csv(input_file_path)
            logging.info('Reading the dataset as DF')

            os.makedirs(os.path.dirname(
                self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,
                      index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(
                df, test_size=TEST_SIZE, random_state=42)

            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)

            logging.info("Data ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data)

    model_trainer = ModelTrainer()
    r2_score_value = model_trainer.initiate_model_trainer(
        train_array=train_arr, test_array=test_arr)
    print(f"r2_score_value: {r2_score_value}")
