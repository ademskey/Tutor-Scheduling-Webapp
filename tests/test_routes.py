import pytest
from config import Config
import os


class TestConfig(Config):
    
    #implement the database url
    
    SECRET_KEY = 'bad-bad-key'
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True