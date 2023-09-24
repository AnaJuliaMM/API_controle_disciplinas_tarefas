from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.student import StudentSerializer
from api.models.student import StudentModel
from rest_framework.exceptions import ValidationError

class StudentView(APIView):
    """
        List all students or create a new student.
    """

    def post(self, request, format=None):
        """
            Method receives a http POST request and format type and create a student object
        """
        try:
            #Gets the data from the request and serialize it
            serializer = StudentSerializer(data=request.data)
            #Validates the data serialized or raise an exception of ValidantionError
            serializer.is_valid(raise_exception=True)
            #Saves the new object in the database
            serializer.save()
            #Returns a sucess message
            return Response({"message": "Student created sucessfully", "data": serializer.data }, status=status.HTTP_201_CREATED)
        #Catches an error raised in the serializer validation
        except ValidationError as e:
            #Returns a dictionary with the exception name and its detail
            return Response({"message": "Validation error", "detail": e.args}, status=status.HTTP_400_BAD_REQUEST)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to create the object", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    
    def get(self, request, format=None):
        """
            Method receives a http GET request and returns all students in the database
        """
        try:
            #Gets all students objects 
            students = StudentModel.objects.all()
            #Serializes the objects
            serializer = StudentSerializer(students, many=True)
            #Returns the objects serialized and a sucess message
            return Response({"message": "All students returned", "data": serializer.data }, status=status.HTTP_200_OK)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to get objects", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


