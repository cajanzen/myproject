import unittest
from app import app


class BasicTestCase(unittest.TestCase):
    def test_hello(self):
        tester = app.test_client(self)
        resp = tester.get('/', content_type='html/text')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'Hello World!!')


unittest.main()
