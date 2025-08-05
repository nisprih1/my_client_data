import boto3
import requests
import time

# Configuration
file_url = 'http://192.168.29.46:8000/client_data.csv'      # replace with your local IP
bucket_name = 'myc-lient-bucket'                            # replace with your actual S3 bucket
s3_key = 'client-logs/client_data.csv'                      # Your data uploaded in that path at S3

# SETUP AWS S3 CLIENT
s3 = boto3.client('s3')

def download_and_upload():
    try:
        print("Get data from your IP...")
        response = requests.get(file_url)

        if response.status_code == 200:
            with open("temp_client_data.csv", "wb") as f:
                f.write(response.content)

            print("Data Uploading into S3...")
            s3.upload_file("temp_client_data.csv", bucket_name, s3_key)
            print("Your Data Successfully Uploaded.\n")
        else:
            print(f"Error: Status code {response.status_code}")
    except Exception as e:
        print("Exception occurred:", e)

# Auto Loop for when new data coming then updated data uploaded in S3 bucket
# while True:
#     download_and_upload()
#     time.sleep(10)
