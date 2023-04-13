# imports
import datetime
import logging
import os

from dotenv import load_dotenv

# configurations
# load environment variables
load_dotenv()
dbHost = os.getenv('DBHOST')
dbPort = os.getenv('DBPORT')
dbName = os.getenv('DBNAME')
dbUsername = os.getenv('DBUSERNAME')
dbPassword = os.getenv('DBPASSWORD')

# connection to database
SQLALCHEMY_DATABASE_URI = f'postgresql://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# application
HOST = os.getenv('APPLICATIONHOST')
PORT = os.getenv('APPLICATIONPORT')
APPLICATION_ROOT = os.getenv('APIAPPLICATIONROOT')
ENVIRONMENT = os.getenv('ENVIRONMENT')
SECRET_KEY = os.getenv('SECRETKEY')

DEBUG = True
if DEBUG:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s: %(message)s",
        datefmt="%d/%m/%y %H:%M:%S",
    )
else:
    filename = datetime.datetime.now().strftime('%d-%m-%Y')
    logging.basicConfig(
        filename=f"logs/{filename}.log",
        level=logging.WARNING,
        format="%(asctime)s %(levelname)s:\
        %(filename)s %(funcName)s \
        pid:%(process)s module:%(module)s %(message)s",
        datefmt="%H:%M:%S",
    )
