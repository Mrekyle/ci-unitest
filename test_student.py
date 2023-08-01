import unittest
from student import Student

class TestStudent(unittest.TestCase):
    """
    Testing the student class in the student.py file
    """

    def test_full_name(self):
        """
        Checking the student class for a students full name by
        Passing in the name "John Doe".
        
        Then creating an instance of the student data for testing 
        purposes. 
        """
        student = Student('John', 'Doe')
        self.assertEqual(student.full_name, 'John Doe') 
        
    def test_alert_santa(self):
        """
        Testing the naughty_list method and setting the 
        data to True if the student has misbehaved.

        First creating an instance of the student for testing
        purposes
        """
        student = Student('John', 'Doe')
        student.alert_santa()
        
        """
        No need to pass the True or False check. Due to the 
        assertTrue method only looking for a True statement
        assertFalse does the same for the False statement 
        """
        self.assertTrue(student.naughty_list)

    def test_student_email(self):
        student = Student('John', 'Doe')
        self.assertEqual(student.student_email, 'john.doe@email.com')

if __name__ == '__main__':
    unittest.main()
 