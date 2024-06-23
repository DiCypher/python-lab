import unittest
from lab import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 4), 0)
        self.assertEqual(multiply(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()
