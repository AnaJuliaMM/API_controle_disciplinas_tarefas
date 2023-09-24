from django.db import models

class StudentModel (models.Model):
    """
        StudentModel is a model class that represents the Student entity in the database

    Attributes:
        name (charfield): the field represents the student name (NOT NULL, max_lengh=255)
        email (charfield): the field represents the student email (NOT NULL, max_lengh=255)

    Methods
        __str__ (str): returns a string representation of the class


    """
    name = models.CharField(max_length=255, blank=False) 
    email = models.EmailField(unique=True, blank=False)

    def __str__(self):
        #Returns a string description of the entity
        return f"{self.name} (email: {self.email})"

