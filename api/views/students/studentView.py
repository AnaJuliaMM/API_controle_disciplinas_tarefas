from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.student import StudentSerializer
from api.models.student import StudentModel

class StudentView(APIView):
    """
        List all students or create a new student.
    """

    def post(self, request, format=None):
        """
            Method receives a http POST request and format type and create a student object
        
        """
        try:
            #Get the data from the request and serialize it
            serializer = StudentSerializer(data=request.data)
            #Validete the data serialized
            serializer.is_valid(raise_exception=True)
            #Save the new object in the database
            serializer.save()
            return Response({"message": "Student created sucessfully", "data": serializer.data }, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "Failed to create"}, status=status.HTTP_400_BAD_REQUEST)
            
    
    def get(self, request, format=None):
        """
            Method receives a http POST request and format type and return all students in the database
        """
        try:
            #Get all students objects 
            students = StudentModel.objects.all()
            #Serializer the objects
            serializer = StudentSerializer(students, many=True)
            # Return the objects serialized and a sucess message
            return Response({"message": "All students returned", "data": serializer.data }, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Failed"}, status=status.HTTP_400_BAD_REQUEST)


