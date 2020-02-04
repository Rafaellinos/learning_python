import unittest

import main

class TestMain(unittest.TestCase):
    
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        """hiiii"""
        test_num = 10
        result = main.do_stuff(test_num)

        self.assertEqual(result, 15) 
        # make sure that result is equal to 15
    
    def test_do_stuff2(self):
        test_num = 'adhas'
        result = main.do_stuff(test_num)

        self.assertIsInstance(result, ValueError)
        # make sure that return valueerror if give a string to do_stuff
        # return from do_stuff is ValueError

    def test_do_stuff3(self):
        test_num = None
        result = main.do_stuff(test_num)

        self.assertEqual(result, 'Plase enter a number')

    def test_do_stuff4(self):
        test_num = None
        result = main.do_stuff(test_num)

        self.assertEqual(result, 'Plase enter a number')

    def tearDown(self):
        print('cleaning')


if __name__ == '__main__': # make sure that only runs if runs this file (will be main)
    unittest.main() # run all tests in TestMain class

# to run all tests, even to more than 1 file python3 -m unittest -v

"""
test_do_stuff4 (test.TestMain) ... about to test a function
cleaning
ok

----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
"""