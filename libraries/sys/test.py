import unittest

from guessing_game import _randomize, _get_nums, main

class Test(unittest.TestCase):
    def setUp(self):
        print("about to start")

    def test_get_nums(self):
        pass

    def test_radomize(self):
        random = _randomize(1, 5)
        self.assertTrue((1 <= random <= 5))

    def test_randomize_string(self):
        result = _randomize('string')
        self.assertIsInstance(result, ValueError)
    
    def test_randomize_string(self):
        result = _randomize('string', 'string')
        self.assertEqual(result, "Must be int")

    def test_randomize_none(self):
        result = _randomize(None)
        self.assertEqual(result, "Cannot have None object")

    def test_randomize_float(self):
        result = _randomize(1.0, 5.0)
        self.assertEqual(result, "Must be int")

    def test_randomize_bool(self):
        result = _randomize(False, True)
        self.assertEqual(result, "Must be int")


    def tearDown(self):
        print('cleaning')


if __name__ == '__main__':
    unittest.main()
