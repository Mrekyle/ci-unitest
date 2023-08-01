import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

class TestStudent(unittest.TestCase):
    """
    Testing the student class in the student.py file
    """

    """
    The general set up function for the start of the testing process
    allows the developer to define variables that are to be used 
    over and over again. Meaning no repeated code. 
    
    Such as defining the instance of the student to be used in all 
    the tests 
    """
    def setUp(self):
        print('Setting up the testing process')
        self.student = Student('John', 'Doe')

    """
    The tear down function is the end of the testing process.
    This will essentially reset anything/delete anything that was
    created during the testing process. 
    """
    def tearDown(self):
        print('Tear Down Function')

    def test_full_name(self):
        """
        Checking the student class for a students full name by
        Passing in the name "John Doe".
        
        Then creating an instance of the student data for testing 
        purposes. 

        Adding the print statement to see what test has been run
        and when it has been run. Allowing more visibility to the 
        testing process in the terminal 
        """
        print('Testing Full Name')
        #  student = Student('John', 'Doe')
        self.assertEqual(self.student.full_name, 'John Doe') 
        
    def test_alert_santa(self):
        """
        Testing the naughty_list method and setting the 
        data to True if the student has misbehaved.

        First creating an instance of the student for testing
        purposes
        """
        print('Testing Alert Santa')
        #  student = Student('John', 'Doe')
        self.student.alert_santa()
        
        """
        No need to pass the True or False check. Due to the 
        assertTrue method only looking for a True statement
        assertFalse does the same for the False statement 
        """
        self.assertTrue(self. student.naughty_list)

    def test_student_email(self):
        """
        Testing the students email address by checking if the 
        outputted value is equal to the string defined in the 
        student class from the other file
        """
        print('Testing Student Email')
        #  student = Student('John', 'Doe')
        self.assertEqual(self.student.student_email, 'john.doe@email.com')

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    def test_course_schedule_success(self):
        print('Testing course Schedule')
        """
        Using the patch method from unittest mock we can mock requests from things
        such as an api/database by filling the date inside of the function
        """
        with patch("student.requests.get") as mocked_get:
            # Mocking the response from an api
            mocked_get.returned_value.ok = True
            # mMocking the text response from an api
            mocked_get.returned_value.text = 'Success'

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, 'Success')
    
    def test_course_schedule_fail(self):
        """
        Testing if the response from the api has failed by using the
        mock testing method
        """
        print('Testing course schedule fail response')

        with patch("student.requests.get") as mocked_get:
            mocked_get.returned_value.ok = False
            mocked_get.returned_value.text = 'Something has gone wrong here'

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, 'Something has gone wrong here')


if __name__ == '__main__':
    unittest.main()
 