# Productivity-Assistant

# How to run
### STEPS:

Clone the repository

```bash
github.com/Sahilraj3107/Productivity-Assistant
```
### STEP 01- Create a conda enviroment after opening the repositary

```bash
# conda activate -n agentapp python=3.12 -y
python -m venv agentapp
```

```bash
# conda activate agentapp
agentapp\Scripts\activate

```

```bash
# creating a file name template.py
python template.py

# If want to add one more file just write in template.py and run the same cmd

# To see chane in github do the following step
git add .
git commit -m "folder structure added"
git push origin main

# refresh and check the repo in github
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


Now,
```bash
# Start the flask Server
python app.py
```

# AWS-CICD-Deployment-with-GitHub-Actions

## 1. Login to AWS console

## 2. Create IAM user for deployment

    #with specific access

    1. EC2 access : It is virtual machine

    2. ECR: Elastic Container registry to save your docker image in aws


    #Description: About the deployment

    1. Build docker image of the source code

    2. Push your docker image to ECR

    3. Launch Your EC2

    4. Pull Your Image from ECR to EC2

    5. Launch your docker image in EC2

    #Policy:

    1. AmazonEC2ContainerRegistryFullAccess

    2. AmazonEC2FullAccess

##  3. Create ECR repo to store/save docker image
    -Save the URL: XXXXXXXXX531.dkr.ecr.eu-north-1.amazonaws.com/{name_the_repo}

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:


       #optional

       sudo apt-get update -y

       sudo apt-get upgrade

       #required

       curl -fsSl https://get.docker.com -o get-docker.sh

       sudo sh get-docker.sh

       sudo usermod -aG docker ubuntu

       newgrp docker

# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one        
