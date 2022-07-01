import unittest


class TestStringUpper(unittest.TestCase):
    def test_normal(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main(verbosity=3)
