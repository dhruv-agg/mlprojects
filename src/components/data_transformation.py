import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object
from src.configs.config import ARTIFACTS_FOLDER_NAME, PROPROCESSOR_FILE_NAME, NUMERICAL_COLUMNS, CATEGORICAL_COLUMNS, TARGET_COLUMN_NAME


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join(
        ARTIFACTS_FOLDER_NAME, PROPROCESSOR_FILE_NAME)


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation

        '''
        try:
            numerical_columns = NUMERICAL_COLUMNS
            categorical_columns = CATEGORICAL_COLUMNS
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )
            logging.info(f"Numerical columns: {NUMERICAL_COLUMNS}")
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info(f"Categorical columns: {CATEGORICAL_COLUMNS}")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, NUMERICAL_COLUMNS),
                    ("cat_pipelines", cat_pipeline, CATEGORICAL_COLUMNS)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = TARGET_COLUMN_NAME
            numerical_columns = NUMERICAL_COLUMNS

            input_feature_train_df = train_df.drop(
                columns=[TARGET_COLUMN_NAME], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN_NAME]

            input_feature_test_df = test_df.drop(
                columns=[TARGET_COLUMN_NAME], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN_NAME]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(
                input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(
                input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr,
                             np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
