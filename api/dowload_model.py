# Load Our model from s3
import boto3

def dowload_model_from_s3():
    """ dowload model from s3 """

    BUCKET_NAME= "mo-churn-bucket"
    MODEL_KEY = "logistic_regression_model.joblib"
    LOCAL_FILE = "logistic_regression_model.joblib"

    # s3 client
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, MODEL_KEY, LOCAL_FILE)

# RUN THE FUNCTION
dowload_model_from_s3()