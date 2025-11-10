# Week 1: Data Ingestion & Storage to AWS S3

# - Data Ingestion

1 - Bringing in the data into the enviroment - import libraries (Toolkit) - Loaded the data - Read out the data

# - Data Storage

2 - Store that data into the cloud - store the data into a S3 bucket (lives in AWS)

    **Prerequisites**
    - [ ] AWS Account created
    - [ ] AWS CLI installed
    - [ ] installed boto3

    ** Configuration **
    - [ ] Created a AWS user
    - [ ] Obtained the authentication credentials (IAM)
            - [ ] Access token
            - [ ] secret key
            - [ ] Added S3 full access permission
            - [ ] configure our credentials to our environment
                - [ ] aws configure
                - [ ] fill in your Access token & secret key
                - [ ] aws sts caller-identity


    ## Store the Data to S3
        - First Method
            - Direct upload
                - login into the console
                - upload from your PC

        - Second Method
            - CLI
               - use the terminal to upload
               - aws s3 ls (helps us list all available s3 buckets)
               - aws s3 mb s3://mo-churn-bucket --region us-east-1
               - aws s3api put-object --bucket mo-churn-bucket --key raw/
               - aws s3 cp Telco-customer-churn s3://mo-churn-bucket/raw/telco-customers.csv

        - Third Method
            - Script (Boto3)
               - wrote a script Using Boto3 (Library that helps your connect to AWS)

- NOTE

- ✅ Use CLI when:

- Quick one-time uploads
- Working directly in terminal

- ❌ Don't use CLI when:

- Need programmatic control in Python
- Want to integrate with data pipelines
- Need to process data before/after upload

# Week 2 - Data Processing & Feature Engineering

- loading the data from S3 bucket
- Understand the data
- Clean the data
- EDA (Exploratory Data analysis) + Feature engineering

# Week 3 - Machine Learning Model training

- Setup & Load Processed Data
- Prepare Data for Modeling (prepare the data for ML model)
- Split Data - Train & Test
- Train Models
- Evaluate Models
- Pick the Best Model
- Save the Model

# Week 4 : Model Deployment -- FastAPI

- What is an API
- Setup FastAPI framework
- create a simple API
- Load our Model
- Accept customer data
- return predictions
- Test API
