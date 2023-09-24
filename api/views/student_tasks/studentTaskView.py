from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models.task import TaskModel
from api.serializers.task import TaskSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from api.models.student import StudentModel





class StudentTaskView(APIView):
    """
    List all tasks for a given student.
    """
    def get(self, request, pk, format=None):
        """
            Returns a JSON of the object that contains the primary key handled by the url  

            Args:
            pk(int)  a value that represents the object pk

        """
        try:
            #Verifies if the student exists
            get_object_or_404(StudentModel, pk=pk) 
            #Gets all tasks objects related to the student
            tasks = TaskModel.objects.filter(student = pk)
            #Serializes the objects
            serializer = TaskSerializer(tasks, many=True)
            #Returns the tasks found
            return Response({"message": "All tasks returned", "data": serializer.data }, status=status.HTTP_200_OK)
        #Catches a exception raised in case of the student does not exist
        except Http404:
            #Retuns a error message with the error explanation 
            return Response({"message": "Student does not exist"}, status=status.HTTP_404_NOT_FOUND)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to get objects", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)