DATA_FOLDER = "src/data"
RAW_DATA_FILE_NAME = 'stud.csv'
TRAIN_DATA_FILE_NAME = 'train.csv' 
TEST_DATA_FILE_NAME = 'test.csv'
ARTIFACTS_FOLDER_NAME = 'artifacts'
ARTIFACTS_RAW_DATA_FILE_NAME = 'data.csv'
PROPROCESSOR_FILE_NAME = "proprocessor.pkl"
MODEL_FILE_NAME = "model.pkl"
TEST_SIZE = 0.2
MODEL_SCORING_THRESHOLD = 0.6

NUMERICAL_COLUMNS = ["writing_score", "reading_score"]
CATEGORICAL_COLUMNS = [
    "gender",
    "race_ethnicity",
    "parental_level_of_education",
    "lunch",
    "test_preparation_course",
]
TARGET_COLUMN_NAME = "math_score"
