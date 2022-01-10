from io import StringIO
import sys
import unittest

from basic_printing import basic_printing, printing_input

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def test_basic_printing(self):
        basic_printing()
        self.assertEqual(self.captured_output.getvalue().strip(), "Hello world.")

    def test_printing_input(self):
        printing_input("Adam")
        self.assertEqual(self.captured_output.getvalue().strip(), "Hello Adam, how are you?")
    
    def tearDown(self):
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main(verbosity=2)