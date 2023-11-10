import unittest
from ../models import BaseModel

class Test_baseModel(unittest.TestCase):
   
    def test_class(self):
        myModel = BaseModel()
        self.assertIsInstance(myModel, BaseModel)


