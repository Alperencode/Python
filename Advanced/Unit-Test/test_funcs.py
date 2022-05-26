import unittest
import main

class TestFuncs(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(10, 5), 15)
        self.assertEqual(main.add(-1, 1), 0)
        self.assertEqual(main.add(-1, -1), -2)
    
    def test_sub(self):
        self.assertEqual(main.sub(10, 5), 5)
        self.assertEqual(main.sub(-1, 1), -2)
        self.assertEqual(main.sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(main.mul(10, 5), 50)
        self.assertEqual(main.mul(-1, 1), -1)
        self.assertEqual(main.mul(-1, -1), 1)
    
    def test_div(self):
        self.assertEqual(main.div(10, 5), 2)
        self.assertEqual(main.div(-1, 1), -1)
        self.assertEqual(main.div(-1, -1), 1)
        self.assertEqual(main.div(5, 0), "error")

if __name__ == "__main__":
    unittest.main()