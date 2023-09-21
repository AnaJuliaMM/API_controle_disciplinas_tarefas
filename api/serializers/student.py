from rest_framework import serializers
from ..models.student import StudentModel
from .task import TaskSerializer


class StudentSerializer(serializers.ModelSerializer):
    """
        Class that transalate entities from JSON structure to python object structure during database communication

        Attribute:  
            tasks: a field that serialize all tasks onjects related to the student model

        It contains an internal class called Meta, that defines the model class and the fields to be serialized
    """
    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = StudentModel
        fields = "__all__" #fields to be serialized