import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://ka7618:Lera)^2000@77.47.192.87:33321/skiresorts'
    #SQLALCHEMY_DATABASE_URI = 'mysql://ka7618:Lera)^2000@10.35.2.26:33321/skiresorts'
    SQLALCHEMY_TRACK_MODIFICATIONS = False