import unittest

from django.test import TestCase
from rest_framework.test import APIClient, RequestsClient

from .utils import Converter


class ConverterTests(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()

    def test_integer_to_english_0(self):
        self.assertEqual(self.converter.integer_to_english(0), "zero")

    def test_integer_to_english_1(self):
        self.assertEqual(self.converter.integer_to_english(1), "one")

    def test_integer_to_english_10(self):
        self.assertEqual(self.converter.integer_to_english(10), "ten")

    def test_integer_to_english_15(self):
        self.assertEqual(self.converter.integer_to_english(15), "fifteen")

    def test_integer_to_english_20(self):
        self.assertEqual(self.converter.integer_to_english(20), "twenty")

    def test_integer_to_english_29(self):
        self.assertEqual(self.converter.integer_to_english(29), "twenty nine")

    def test_integer_to_english_50(self):
        self.assertEqual(self.converter.integer_to_english(50), "fifty")

    def test_integer_to_english_59(self):
        self.assertEqual(self.converter.integer_to_english(59), "fifty nine")

    def test_integer_to_english_80(self):
        self.assertEqual(self.converter.integer_to_english(80), "eighty")

    def test_integer_to_english_89(self):
        self.assertEqual(self.converter.integer_to_english(89), "eighty nine")

    def test_integer_to_english_101(self):
        self.assertEqual(self.converter.integer_to_english(101), "one hundred one")

    def test_integer_to_english_151(self):
        self.assertEqual(
            self.converter.integer_to_english(151), "one hundred fifty one"
        )

    def test_integer_to_english_501(self):
        self.assertEqual(self.converter.integer_to_english(501), "five hundred one")

    def test_integer_to_english_551(self):
        self.assertEqual(
            self.converter.integer_to_english(551), "five hundred fifty one"
        )

    def test_integer_to_english_1001(self):
        self.assertEqual(self.converter.integer_to_english(1001), "one thousand one")

    def test_integer_to_english_1234(self):
        self.assertEqual(
            self.converter.integer_to_english(1234),
            "one thousand two hundred thirty four",
        )

    def test_integer_to_english_12345(self):
        self.assertEqual(
            self.converter.integer_to_english(12345),
            "twelve thousand three hundred forty five",
        )

    def test_integer_to_english_123456(self):
        self.assertEqual(
            self.converter.integer_to_english(123456),
            "one hundred twenty three thousand four hundred fifty six",
        )

    def test_integer_to_english_1234567(self):
        self.assertEqual(
            self.converter.integer_to_english(1234567),
            "one million two hundred thirty four thousand five hundred sixty seven",
        )

    def test_integer_to_english_12345678(self):
        self.assertEqual(
            self.converter.integer_to_english(12345678),
            "twelve million three hundred forty five thousand six hundred seventy eight",
        )

    def test_integer_to_english_123456789(self):
        self.assertEqual(
            self.converter.integer_to_english(123456789),
            "one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine",
        )

    def test_integer_to_english_1234567890(self):
        self.assertEqual(
            self.converter.integer_to_english(1234567890),
            "one billion two hundred thirty four million five hundred sixty seven thousand eight hundred ninety",
        )

    def test_integer_to_english_1234567890123(self):
        self.assertEqual(
            self.converter.integer_to_english(1234567890123),
            "Sorry... Cannot convert a number greater than 999999999999",
        )


class GETNumToEnglishTests(TestCase):
    def setUp(self):
        self.client = RequestsClient()

    def test_get_valid_query(self):
        response = self.client.get("http://127.0.0.1:8000/num_to_english?number=23")
        self.assertEqual(response.status_code, 200)

    def test_get_valid_query_content(self):
        response = self.client.get("http://127.0.0.1:8000/num_to_english?number=23")
        content = response.json()
        expected = {"status": "ok", "number": "twenty three"}
        for field, value in expected.items():
            with self.subTest():
                self.assertEqual(content[field], value)

    def test_get_invalid_query(self):
        response = self.client.get("http://127.0.0.1:8000/num_to_english?number=abc")
        self.assertEqual(response.status_code, 400)

    def test_get_invalid_query_content(self):
        response = self.client.get("http://127.0.0.1:8000/num_to_english?number=abc")
        content = response.json()
        expected = {
            "status": "Error",
            "message": "Please insert an integer number between 0-999999999999",
        }
        for field, value in expected.items():
            with self.subTest():
                self.assertEqual(content[field], value)

    def test_get_invalid_query_negative_number_content(self):
        response = self.client.get("http://127.0.0.1:8000/num_to_english?number=-23")
        content = response.json()
        expected = {
            "status": "Error",
            "message": "Please insert an integer number between 0-999999999999",
        }
        for field, value in expected.items():
            with self.subTest():
                self.assertEqual(content[field], value)


class POSTNumToEnglishTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_post_valid_payload(self):
        response = self.client.post(
            "http://127.0.0.1:8000/num_to_english/", {"number": "23"}, format="json"
        )
        self.assertEqual(response.status_code, 200)

    def test_post_valid_payload_content(self):
        response = self.client.post(
            "http://127.0.0.1:8000/num_to_english/", {"number": "23"}, format="json"
        )
        content = response.json()
        expected = {"status": "ok", "number": "twenty three"}
        for field, value in expected.items():
            with self.subTest():
                self.assertEqual(content[field], value)

    def test_post_invalid_payload(self):
        response = self.client.post(
            "http://127.0.0.1:8000/num_to_english/", {"number": "23abc"}, format="json"
        )
        self.assertEqual(response.status_code, 400)

    def test_post_invalid_payload_content(self):
        response = self.client.post(
            "http://127.0.0.1:8000/num_to_english/", {"number": "23abc"}, format="json"
        )
        content = response.json()
        expected = {
            "status": "Error",
            "message": "This is not a valid payload",
            "number": "Should be a string of a number between 0-999999999999",
        }
        for field, value in expected.items():
            with self.subTest():
                self.assertEqual(content[field], value)

    def test_post_invalid_payload_negative_number_content(self):
        response = self.client.post(
            "http://127.0.0.1:8000/num_to_english/", {"number": "-23"}, format="json"
        )
        content = response.json()
        expected = {
            "status": "Error",
            "message": "This is not a valid payload",
            "number": "Should be a string of a number between 0-999999999999",
        }
        for field, value in expected.items():
            with self.subTest():
                self.assertEqual(content[field], value)
