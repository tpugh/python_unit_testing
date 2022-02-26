#test_tutorial.py
from tutorial import say_hello
from unittest import TestCase
from io import StringIO
from unittest.mock import patch


class PrintingTest(TestCase):

    def test_say_hello(self):
        try:
            say_hello(name='')
        except Exception:
            self.fail('should not fail')
