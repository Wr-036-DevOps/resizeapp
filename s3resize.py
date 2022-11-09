import boto3
import sys
import os 
from PIL import Image
from dotenv import load_dotenv



basewidth = 50
img = Image.open('Filename - File to resize')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
img.save('file')

load_dotenv() # this loads the .env file with our credentials

session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

s3 = session.resource('s3')

# Bucket - Bucket to upload to (the top level directory under AWS S3)
# Key - S3 object name (can contain subdirectories). If not specified then file_name is used

s3.meta.client.upload_file(Filename='Filename - File to upload', Bucket='s3 bucket name', Key='name of the file')