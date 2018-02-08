import unittest
from app.src.app import sum_both


class AddTest(unittest.TestCase):
    def test_sum_both(self):
        self.assertEqual(sum_both(2, 2), 4)
        self.assertEqual(sum_both(4, 4), 8)
        self.assertEqual(sum_both(-1, 3), 2)
        self.assertEqual(sum_both(4, -1), 3)
        self.assertEqual(sum_both(3, 1), 4)
        self.assertEqual(sum_both(1.0, 1), 2)
        self.assertEqual(sum_both(1.2, 2.1), 3.3)
        self.assertEqual(sum_both(0.5, 2.1), 2.6)
        self.assertEqual(sum_both(1.2, 0), 1.2)
        self.assertEqual(sum_both(1.5, 0.6), 2.1)


if __name__ == '__main__':
    unittest.main()