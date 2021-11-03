"""
#
# @File         : Student.py
# @Created      : 2021-11-01 11:18
# @Author       : Bubashankushan B
# @Version      : v1.0.0
# @Licensing    : 
#
# @Description  :
#
"""


# Student class created
class Student:

    def __init__(self, fn: str = "", ln: str = ""):  # Initialise function with string annotation
        self._firstName = fn
        self._lastName = ln

    # Create a getter function
    @property
    def firstName(self):
        return self._firstName  # getter

    # Create the setter function
    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName

    @property
    def lastName(self):
        return self._lastName  # getter

    # Create the setter function
    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    def displayStudentName(self):
        print("Student Name : {}".format(self._firstName + " " + self._lastName))
