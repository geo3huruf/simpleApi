import os

class Config(object):
    SECRET_KEY = os.environ.get('4AEE18F83AFDEB23') or 'you-will-never-guess'
