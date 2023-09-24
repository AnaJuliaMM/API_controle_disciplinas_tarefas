from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.task import TaskSerializer
from api.models.task import TaskModel
from rest_framework.exceptions import ValidationError


class TaskView(APIView):
    """
        List all tasks or create a new task.
    """

    def post(self, request, format=None):
        """
            Method receives a http POST request and format type and create a task object
        
        """
        try:
            #Gets the data from the request and serialize it
            serializer = TaskSerializer(data=request.data)
            #Validates the data serialized or raise an exception of ValidantionError
            serializer.is_valid(raise_exception=True)
            #Saves the new object in the database
            serializer.save()
            #Returns a sucess message
            return Response({"message": "Task created sucessfully", "data": serializer.data }, status=status.HTTP_201_CREATED)
        #Catches the error raised in the serializer validation
        except ValidationError as e:
            #Returns a dictionary with the exception name and its detail
            return Response({"message": "Validation error", "detail": e.args}, status=status.HTTP_400_BAD_REQUEST)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to create the object", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    
    def get(self, request, format=None):
        """
            Method receives a http POST request and format type and return all task in the database
        """
        try:
            #Gets all students objects 
            students = TaskModel.objects.all()
            #Serializes the objects
            serializer = TaskSerializer(students, many=True)
            #Returns the objects serialized and a sucess message
            return Response({"message": "All tasks returned", "data": serializer.data }, status=status.HTTP_200_OK)
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to get objects", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


