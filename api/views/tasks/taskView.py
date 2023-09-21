from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from api.serializers.task import TaskSerializer
from api.models.task import TaskModel
from api.models.student import StudentModel

class TaskView(APIView):
    """
        List all tasks or create a new task.
    """

    def get_object(self, pk, model):
        """
            Return a object by its primary key
        Args:
            pk : a value that represents the object pk
        """
        try:
            return model.objects.get(pk=pk)
        except:
            raise Http404


    def post(self, request, format=None):
        """
            Method receives a http POST request and format type and create a task object
        
        """
        try:
            student = self.get_object(request.data.get("student"), StudentModel)
            #Get the data from the request and serialize it
            serializer = TaskSerializer(data=request.data)
            #Validete the data serialized
            serializer.is_valid(raise_exception=True)
            #Save the new object in the database
            serializer.save(student=student)
            return Response({"message": "Task created sucessfully", "data": serializer.data }, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "Failed to create"}, status=status.HTTP_400_BAD_REQUEST)
            
    
    def get(self, request, format=None):
        """
            Method receives a http POST request and format type and return all task in the database
        """
        try:
            #Get all students objects 
            students = TaskModel.objects.all()
            #Serializer the objects
            serializer = TaskSerializer(students, many=True)
            # Return the objects serialized and a sucess message
            return Response({"message": "All tasks returned", "data": serializer.data }, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Failed"}, status=status.HTTP_400_BAD_REQUEST)

