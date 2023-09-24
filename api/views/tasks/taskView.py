from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.task import TaskSerializer
from api.models.task import TaskModel
from rest_framework.exceptions import ValidationError
from django.http import Http404
from api.models.student import StudentModel
from api.models.subject import SubjectModel




class TaskView(APIView):
    """
        List all tasks or create a new task.
    """

    def get_student(self, pk):
        """
            Return a Student object by its primary key
        Args:
            pk : a value that represents the object pk
        """
        try:
            #Gets a object by its primary key
            return StudentModel.objects.get(pk=pk)
        except:
            #Raises a Http404  exception in case of not found
            raise Http404('Student not found')
        
    def get_subjects(self, pk):
        """
            Return a list of Subject objects by its primary keys
        Args:
            pk : a value that represents the object pk
        """
        try:
            #Gets a object by its primary key
            return SubjectModel.objects.filter(pk__in = pk)
        except:
            #Raises a Http404  exception in case of not found
            raise Http404('Subjects not found')
        
        

    def post(self, request, format=None):
        """
            Method receives a http POST request and format type and create a task object
        
        """
        try:
            #Calls the method that gets the student object by its pk
            student = self.get_student(request.data.get("student"))
            #Calls the method that gets the subjects object by its pk
            subjects = self.get_subjects(request.data.get("subjects"))
            #Gets the data from the request and serialize it
            serializer = TaskSerializer(data=request.data)
            #Validates the data serialized or raise an exception of ValidantionError
            serializer.is_valid(raise_exception=True)
            #Saves the new object in the database
            serializer.save(student=student, subjects=subjects)
            #Returns a sucess message and the object created
            return Response({"message": "Task created sucessfully", "data": serializer.data }, status=status.HTTP_201_CREATED)
        #Catches a exception raised in case of the object does not exist
        except Http404 as e:
            #Retuns a error message with the error explanation 
            return Response({"message": e.args}, status=status.HTTP_404_NOT_FOUND)
        #Catches the error raised in the serializer validation
        except ValidationError as e:
            #Returns a dictionary with the exception name and its detail(e.args)
            return Response({"message": "Validation error", "detail": e.args}, status=status.HTTP_400_BAD_REQUEST)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation (e.args) and server side code
            return Response({"message": "Failed to create the object", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    
    def get(self, request, format=None):
        """
            Method receives a http GET request and returns all tasks in the database
        """
        try:
            #Gets all students objects 
            students = TaskModel.objects.all()
            #Serializes the objects
            serializer = TaskSerializer(students, many=True)
            #Returns the objects serialized and a sucess message
            return Response({"message": "All tasks returned", "data": serializer.data }, status=status.HTTP_200_OK)
        except Exception as e:
            #Retuns a error message with the error explanation (e.args) and server side code
            return Response({"message": "Failed to get objects", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


