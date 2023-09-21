from rest_framework import serializers
from ..models.subject import SubjectModel
from .task import TaskSerializer


class SubjectSerializer(serializers.ModelSerializer):
    """
        Class that transalate entities from JSON structure to python object structure during database communication

        Attribute:  
            tasks: a field that serialize all tasks onjects related to the subject model

        It contains an internal class called Meta, that defines the model class and the fields to be serialized
    """

    class Meta:
        model = SubjectModel
        fields = "__all__" #fields to be serialized