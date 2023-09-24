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
            #Gets all tasks objects 
            tasks = TaskModel.objects.filter(student = pk)
            #Serializes the objects
            serializer = TaskSerializer(tasks, many=True)
            #Returns the tasks found
            return Response({"message": "All tasks returned", "data": serializer.data }, status=status.HTTP_200_OK)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to get objects", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)