"""

When using building tests for python. The standard file naming is:

test_FILENAME.py

As this tells everyone looking at the code and files that this is the python testing 
for that specific file of the application

"""

import unittest  # allows the use of the unittest framework.
from evens import even_number_of_evens  # importing the function from the other file

class TestEvens(unittest.TestCase):
    # pass - allows the file to be run error free if there is no code inside of the function

    # testing if the functions are linked correctly
    # def test_function_returns_True(self):
    #     self.assertTrue(even_number_of_evens([]))

    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    """
    Below is checking to see 
    if the function was passed an empty list
    if the function was passed 2 numbers
    if the function was passed 1 number
    if the function was passed multiple odd numbers 
    """

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)

if __name__ == '__main__':
    unittest.main()
  