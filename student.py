from datetime import date, timedelta
import requests

class Student:
    """
    A student class as a base for method testing
    """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        # sets the start date to the time that the unit was created/application was run
        self._start_date = date.today()
        # sets the end date of the students time to 365 days from the date of creation using timedelta
        self.end_date = date.today() + timedelta(days=365) 
        self.naughty_list = False
        

        """
        Returns the full name of the student 
        """
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True  

    """
    As its a read only method the property decorator indicates
    this

    Using the .lower() method as all email address use lowercase letters
    """
    @property
    def student_email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=5)

    def course_schedule(self):
        response = requests.get(f"http://www.mycompanyname.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text 
        else:
            return "Something went wrong here"

  