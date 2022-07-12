import unittest
from handler import hello

class TestHello(unittest.TestCase):

    def test_hello_function(self):
        event = {}
        context = {}
        actual = hello(event, context)
        expected = {'statusCode': 200, 'body': '{"message": "Go Serverless v1.0! Your function executed successfully!", "input": {}}'}
        print(actual)
        self.assertEqual(expected, actual)