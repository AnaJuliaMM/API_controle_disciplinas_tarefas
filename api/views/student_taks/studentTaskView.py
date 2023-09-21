from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.task import TaskModel
from api.serializers.task import TaskSerializer


class StudentTaskView(APIView):
    """
    List all tasks for a given student.
    """
    def get(self, request, pk, format=None):
        try: 
            tasks = TaskModel.objects.filter(student = pk)
            serialize = TaskSerializer(tasks, many=True)
            return Response(serialize.data)
        except:
            return Response({"message": "Tasks not found"}, status=status.HTTP_400_BAD_REQUEST)