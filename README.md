# End-to-end-Hate-Classification-Project


git clone https://github.com/Abhishek-guptaaa/End-to-end-Hate-Classification-Project.git

conda activate venv/

pip install -r requirements.txt

python mongo.py

python hate\components\data_ingestion.py

python main.py

python hate\pipelines\training_pipeline.py

streamlit run app.py

# AWS-CICD-Deployment-with-Github-Actions
## 1. Login to AWS console.

## 2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
- Save the URI: 730335610052.dkr.ecr.us-east-1.amazonaws.com/nlp_project

# 4. Create EC2 machine (Ubuntu)

# 5. Open EC2 and Install docker in EC2 Machine:

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

# 6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one

# 7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI =   730335610052.dkr.ecr.us-east-1.amazonaws.com
ECR_REPOSITORY_NAME = nlp_project


Note: Streamlit run on this port: 8501
