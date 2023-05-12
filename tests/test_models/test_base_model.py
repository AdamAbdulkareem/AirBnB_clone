#!/usr/bin/python3
import unittest
import datetime
import models
from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):

    def test_created_at(self):
        my_instance = BaseModel()
        result = my_instance.created_at
        excepted_result = datetime.datetime.now()
        self.assertEqual(result, excepted_result)
        self.assertIs(type(result), datetime.datetime)

    def test_updated_at(self):
        my_instance = BaseModel()
        my_instance.save()
        result = my_instance.updated_at
        excepted_result = datetime.datetime.now()
        self.assertEqual(result, excepted_result)
        self.assertIs(type(result), datetime.datetime)
        
    def test_to_dict(self):
        my_instance = BaseModel()
        result = my_instance.to_dict()
        expected_result = my_instance.__dict__
        self.assertEqual(result, expected_result)
        
    def test___init__(self):
        my_instance = BaseModel(first_name="Adam", last_name="Abdulkareem")
        self.assertEqual(my_instance.first_name, "Adam")
        self.assertEqual(my_instance.last_name, "Abdulkareem")

if __name__ == '__main__':
    unittest.main()
