from django.db import models

class SubjectModel (models.Model):
    """
        SubjectModel is a model class that represents the Subject entity in the database

    Attributes:
        name (charfield): the field represents the subject name (NOT NULL, max_lengh=150)
        description (charfield): the field contains a description of the subject (NOT NULL, max_lengh=255)

    Methods
        __str__ (str): returns a string representation of the class


    """
    name = models.CharField(max_length=150, blank=False) 
    description = models.CharField(max_length=255, blank=False)

    def __str__(self):
        #Returns a string description of the entity
        return f"Subject {self.name} :  {self.description})"

