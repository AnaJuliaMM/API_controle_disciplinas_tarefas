from rest_framework import serializers
from ..models.task import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    """
        Class that transalate entities from JSON structure to python object structure during database communication

        It contains an internal class called Meta, that defines the model class and the fields to be serialized
    """
    #Instead of printing the student's pk, prints the string set in the __str__ method
    student = serializers.StringRelatedField(read_only=True)
    #Instead of printing the subject's id, prints the value of the field name
    subjects = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        model = TaskModel
        fields = "__all__" #fields to be serialized