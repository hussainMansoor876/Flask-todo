import unittest
import sys,json
from app import app

class TestMethods(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"]=True
        self.app=app.test_client()


    def tearDown(self):
        pass

    def test_index_get(self):
        response=self.app.get("/todo/api/v1.0/")
        self.assertEqual(response.status_code,200)

    def test_one_get(self):
        response = self.app.get("/todo/api/v1.0/5b75ae8de09ec81d1cc35f7a")
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.app.post("/todoAdd")
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        response = self.app.put("/todo/api/v1.0/5b75ae8de09ec81d1cc35f7a" )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()