import unittest
import json
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_quickSort(self):
        response = self.client.post('/api/quickSort', json={"array": [5, 3, 8, 4, 2]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["sortedArray"], [2, 3, 4, 5, 8])

if __name__ == "__main__":
    unittest.main()
