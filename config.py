import os

class Config:
    MONGO_DBNAME = "cooking_book"
    MONGO_URI = os.environ.get("MONGO_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
  
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465 
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
