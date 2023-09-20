from rest_framework import serializers
from ..models.task import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    """
        Class that transalate entities from JSON structure to python object structure during database communication

        It contains an internal class called Meta, that defines the model class and the fields to be serialized
    """

    class Meta:
        model = TaskModel
        fields = "__all__" #fields to be serialized