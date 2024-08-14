# End-to-end-Hate-Classification-Project


git clone https://github.com/Abhishek-guptaaa/End-to-end-Hate-Classification-Project.git

conda activate venv/

pip install -r requirements.txt

python mongo.py

python hate\components\data_ingestion.py

python main.py

python hate\pipelines\training_pipeline.py

streamlit run app.py