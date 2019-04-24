import unittest
import method

class TestAdd(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(method.add(2,2),4)

if __name__ = "__main__":
    unittest.main()
