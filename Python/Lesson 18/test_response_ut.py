"""
Testing with pytest
"""
import unittest
import requests


BASE_URL = "https://demo.treblle.com/api/v1/"

ARTICLE_DATA = {
        {
                "title": "Test title",
                "content": "condg fsdg sfdg sdfg sdfg sfgasasdfasf a fsf dtent",
                "image": "https://i.pinimg.com/originals/5b/4f/81/5b4f818e91e9df3d02875e8f421100f6.jpg",
                "user": "30563ae9-cea7-4eaa-abfb-197687639e8c"
        }
}
class TestGet(unittest.TestCase):
    def test_get_articles(self):
        """
        """
        response = requests.get(BASE_URL + "articles")
        self.assertEqual(response.status_code, 200)
        self.assertIn("OK",response.reason)

    def test_validate_articles(self):
        response = requests.get(BASE_URL + "articles")
        response_json = response.json()
        self.assertIn("articles",response_json.keys())
        self.assertIn("http",response_json["articles"][0]["image"])





