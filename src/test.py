import unittest
from oper import Operations


class TestUM(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(Operations.sum(3, 4), 7)

    def test_sub(self):
        self.assertEqual(Operations.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(Operations.mul(3, 2), 6)

    def test_div(self):
        self.assertEqual(Operations.div(12, 4), 3)

    def test_square(self):
        self.assertEqual(Operations.square(25), 5)


if __name__ == '__main__':
    unittest.main()
