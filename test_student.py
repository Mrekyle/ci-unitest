import unittest
from student import Student

class TestStudentData(unittest.TestCase):
    """
    Testing the student class in the student.py file
    """

    def test_first_and_last_name(self):
        """
        Creating an instance of the student data for testing 
        purposes. Passing in the name "John Doe"
        """
        student = Student("John", "Doe")

        self.assertEqual(student.full_name, 'John Doe') 
        

if __name__ == '__main__':
    unittest.main()
 