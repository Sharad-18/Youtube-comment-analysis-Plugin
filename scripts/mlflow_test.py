import mlflow
import random
import os

os.environ["MLFLOW_TRACKING_USERNAME"] = "Sharad-18"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "121f36e6a42036e33a56166ed5d1717b205a86b8"


mlflow.set_tracking_uri("https://dagshub.com/Sharad-18/Youtube-comment-analysis-Plugin.mlflow")

with mlflow.start_run():
    mlflow.log_param("param1",random.randint(1,100))
    mlflow.log_param("param2",random.random())
    print("loggesd succefully")