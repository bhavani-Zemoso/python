import mymath
import unittest

class TestAdd(unittest.TestCase):
    
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = mymath.add(2,3)
        self.assertEqual(result, 5)
    
    def test_add_floats(self):
        result = mymath.add(2.5, 3.8)
        self.assertEqual(result, 6.3)
    
    def test_add_strings(self):
        result = mymath.add("abc", "def")
        self.assertEqual(result, "abcdef")

if __name__ == '__main__':
    unittest.main()

