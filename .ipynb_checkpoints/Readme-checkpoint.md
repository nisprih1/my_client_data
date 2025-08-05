# Local Server  to S3 File Uploader

This is a simple Python project that reads a CSV file from your local machine using its IP address and uploads it automatically to an AWS S3 bucket.

---
## Project Overview
- Uses Python’s built-in HTTP server to expose a local CSV file
- A Python script fetches the file via IP and uploads it to AWS S3 using  `boto3`
- Useful for simulating a client machine sending data to cloud storage

---

## ▶ How to Run

### 1. Place your CSV file
Put your `data.csv` in a folder like:
C:\Users\UsersName\My_Client_Data\

### 2. Start local HTTP server
In Command Prompt:

cd C:\Users\UsersName\My_Client_Data\
python -m http.server 8000

### 3. Set up AWS CLI

Run:

aws configure

Enter your AWS access key
secret key
region (e.g. ap-south-1)
and output format (e.g. csv)

### 4. Run the Python script
Update and run `upload_from_ip.py` with your IP and bucket name:

file_url = 'http://<your-ip>:8000/Laptop_data.csv'
bucket_name = 'your-s3-bucket-name'

Run it in terminal or PyCharm:

python upload_from_ip.py

---

## Output

The file will be uploaded to your S3 bucket inside the folder:
client-logs/Laptop_data.csv

---

## Author
Tara Chand Gurjar