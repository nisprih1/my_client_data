#  My Client Data Upload Project

##  Overview
This project automates the process of fetching CSV data from a client (via local or remote HTTP) and uploading it to **AWS S3**.  
It can be run locally or through **AWS CodeBuild** for a fully automated ETL workflow.

---

##  Components

| File | Description |
|------|-------------|
| `upload_from_ip.py` | Python script that downloads CSV from a provided IP/URL and uploads to S3. |
| `client_data.csv` | Sample dataset for testing. |
| `buildspec.yml` | AWS CodeBuild configuration file to automate installation, script execution, and upload to S3. |

---

##  Usage Guide

### Host CSV Locally (Optional Test)
```bash
cd path/to/csv
python3 -m http.server 8000
```
Access in browser or via script:
```
http://<your-ip>:8000/client_data.csv
```

---

### Configure AWS CLI
```bash
aws configure
```
- **Access Key**: Your AWS access key  
- **Secret Key**: Your AWS secret key  
- **Region**: Example `ap-south-1`  
- **Output**: `json`

---

### Update Script Variables
In `upload_from_ip.py`, update:
```python
file_url = "http://<your-ip>:8000/client_data.csv"
bucket_name = "your-s3-bucket"
```

---

### Run Script Locally
```bash
python upload_from_ip.py
```
If the script processes correctly, you’ll see:
```
 File uploaded successfully to S3
```

---

### Run in AWS CodeBuild
The `buildspec.yml` will:
1. Install Python dependencies (`requests`, `boto3`, `pandas`, etc.)
2. Run `upload_from_ip.py`
3. Upload the output CSV to your S3 bucket

**Build command output example:**
```
Installing dependencies...
Running ETL script...
File uploaded successfully
```

---

## Notes
- Ensure `upload_from_ip.py` creates `output_file.csv` or update `buildspec.yml` to upload the correct filename (e.g., `client_data.csv`).
- Make sure your S3 bucket exists before running CodeBuild.

---

## Author
**Tara Chand Gurjar**  
