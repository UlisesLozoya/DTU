"""This file contains all the exercises relating to Student exercise (10.3)."""
class Person:
    """An expanded version of the python str class.""" 

    def __init__(self, first_name:str, last_name:str):
        """Initialize the person class.

        :param first_name: The person's first name
        :param last_name: The person's last name.
        """
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        """Initialize the person class.
        
        :return: The student's full name.
        """
        full_name= self.first_name+ ' ' + self.last_name
        return full_name


class Student(Person):
    """An extended version of the Person class which also includes the degree.""" 

    # TODO: Code has been removed from here. 

        
    
