"""
Testing with pytest
"""
import requests
import pytest


BASE_URL = "https://demo.treblle.com/api/v1/"

# class TestGet:


#     def test_get_articles(self, capsys):
#         response = requests.get(BASE_URL + "articles")
#         print(response)
#         assert response.status_code == 200

def test_get_articles():
        response = requests.get(BASE_URL + "articles")
        print(response)
        # assert response.status_code == 200
        print("Looo")