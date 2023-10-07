import os


class Config:
    IP = 'localhost'
    DEBUG = True
    TESTING = True
    IMG_FOLDER = os.path.join('img')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://' \
                              'postgres:' \
                              'password' \
                              '@localhost:5432/vote'
