from django.db import models
from .student import StudentModel
from .subject import SubjectModel

class TaskModel (models.Model):
    """
        TaskModel is a model class that represents the Task entity in the database

    Attributes:
        title (charfield): the field represents the task  title (NOT NULL, max_lengh=150)
        description (charfield): the field contains the task description (NOT NULL, max_lengh=255)
        deadline(DateField): the field constains the task deadline (NOT NULL)
        done(boolena): the field shows if the task is done or not(NOT NULL, default=False)
        student(fk): it represents the student responsable for the task (cascade delete mode)
        subjects(fk): it represents all subjects related to the task

    Methods
        __str__ (str): returns a string representation of the class


    """
    title = models.CharField(max_length=150, blank=False)    
    description = models.CharField(max_length=255, blank=False)
    deadline = models.DateField(blank=False)
    done = models.BooleanField(default=False, blank=False)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name="tasks")
    subjects = models.ManyToManyField(SubjectModel, related_name="tasks")


    def __str__(self):
        #Returns a string description of the entity
        return f"{self.title}(ddl = {self.deadline}, status = {self.done}): {self.description} "

