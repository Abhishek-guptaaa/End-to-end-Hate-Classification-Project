import streamlit as st
from hate.pipelines.training_pipeline import TrainPipeline
from hate.pipelines.prediction_pipeline import PredictionPipeline
from hate.exception import CustomException

def main():
    st.title("Hate Speech Detection")

    menu = ["Home", "Train", "Predict"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Welcome to the Hate Speech Detection App")
        st.write("This app allows you to train a model for detecting hate speech and make predictions on text data.")
    
    elif choice == "Train":
        st.subheader("Training the Model")
        if st.button("Start Training"):
            try:
                train_pipeline = TrainPipeline()
                train_pipeline.run_pipeline()
                st.success("Training successful!")
            except Exception as e:
                st.error(f"Error Occurred during training: {e}")

    elif choice == "Predict":
        st.subheader("Predict Hate Speech")
        text = st.text_area("Enter text for prediction")
        if st.button("Predict"):
            try:
                prediction_pipeline = PredictionPipeline()
                prediction = prediction_pipeline.predict(text)
                st.write({"text": text, "prediction": prediction})
            except Exception as e:
                st.error(f"Error Occurred during prediction: {e}")

if __name__ == '__main__':
    main()
