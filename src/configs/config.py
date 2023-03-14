DATA_FOLDER = "src/data"
RAW_DATA_FILE_NAME = 'stud.csv'
ARTIFACTS_FOLDER_NAME = 'artifacts'
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
