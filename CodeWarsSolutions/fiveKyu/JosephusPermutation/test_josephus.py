import unittest
from josephus import permute

class permuteTest(unittest.TestCase):
    def test_Permute1(self):
        self.assertEqual(permute([1,2,3,4,5,6], 1), [1,2,3,4,5,6])

if __name__ == "__main__":
    unittest.main()