
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from config.config import Config
from hate.logger import logging
from hate.components.data_ingestion import DataIngestion
from hate.components.data_cleaning import DataCleaning
from hate.components.text_tokenization import TextTokenization
from hate.components.model_training import ModelTraining
from hate.exception import CustomException
import joblib


def main():
    try:
        logging.info("Starting NLP project")

        # Data Ingestion
        data_ingestion = DataIngestion()
        raw_data_path = data_ingestion.initiate_data_ingestion()
        
        # Load the raw data
        raw_data = pd.read_csv(raw_data_path)
        
        # Ensure raw_data is a DataFrame
        if not isinstance(raw_data, pd.DataFrame):
            raise CustomException("Data ingestion did not return a DataFrame", sys)
        
        # Data Cleaning 
        data_cleaning = DataCleaning()
        cleaned_data = data_cleaning.clean_data(raw_data, Config.TWEET)
        
        # Ensure the directory for the cleaned data file exists
        os.makedirs(os.path.dirname(Config.CLEANED_DATA_PATH), exist_ok=True)

        # Save cleaned data to CSV
        cleaned_data.to_csv(Config.CLEANED_DATA_PATH, index=False)
        
        # Split the cleaned data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            cleaned_data[Config.TWEET], cleaned_data[Config.CLASS], test_size=0.2, random_state=42)  
        
        # Save the test data to CSV files
        test_data = pd.DataFrame({Config.TWEET: X_test, Config.CLASS: y_test})
        test_data.to_csv(Config.X_TEST_PATH, index=False)
        logging.info(f"Test data saved at {Config.X_TEST_PATH}")
        
        # Text Tokenization 
        text_tokenization = TextTokenization()
        text_tokenization.fit_tokenizer(X_train)
        sequences_matrix = text_tokenization.transform_texts(X_train)
        
        # Model Training
        model_training = ModelTraining(sequences_matrix, y_train)
        model_training.build_model()
        history = model_training.train_model()  # Corrected line

        # Save the tokenizer
        joblib.dump(text_tokenization.tokenizer, Config.TOKENIZER_PATH)
        logging.info(f"Tokenizer saved at {Config.TOKENIZER_PATH}")

        logging.info("NLP project completed successfully")
    except Exception as e:
        logging.error(f"Error in main script: {e}")
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()
