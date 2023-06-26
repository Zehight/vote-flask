import os


class Config:
    IP = 'localhost'
    DEBUG = True
    TESTING = True
    IMG_FOLDER = os.path.join('img')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://' \
                              'postgres:' \
                              '5YXvsR4IITEoqEDM4QUi' \
                              '@containers-us-west-93.railway.app:6106/railway'