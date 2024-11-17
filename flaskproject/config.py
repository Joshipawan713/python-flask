import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Flask_Sectet_Key')
    # Add more config variables if necessary (e.g., DB connection string)
