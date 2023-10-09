import pytest
import unittest
import warnings
warnings.filterwarnings("ignore")



class TestConfig(Config):
    TESTING = True
    #enter the database link

class TestModels(unittest.TestCase):
    def setUp(self):
        pass

    def test_password_hashing(self):
        pass
   
   
   
if __name__ == '__main__':
    unittest.main(verbosity=2)