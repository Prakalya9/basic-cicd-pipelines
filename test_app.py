
import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("Student"),
            "Hello, Student! CI/CD pipeline is working."
        )

    def test_empty_name(self):
        self.assertEqual(
            greet(""),
            "Hello, ! CI/CD pipeline is working."
        )

if __name__ == "__main__":
    unittest.main()
