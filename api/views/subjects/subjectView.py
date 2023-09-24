from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.subject import SubjectSerializer
from api.models.subject import SubjectModel
from rest_framework.exceptions import ValidationError

class SubjectView(APIView):
    """
        List all subject or create a new subject.
    """

    def post(self, request, format=None):
        """
            Method receives a http POST request and format type and create a subject object
        
        """
        try:
            #Gets the data from the request and serializes it
            serializer = SubjectSerializer(data=request.data)
            #Validates the data serialized or raise an exception of ValidationError
            serializer.is_valid(raise_exception=True)
            #Saves the new object in the database
            serializer.save()
            #Returns a sucess message with the object created
            return Response({"message": "Subject created sucessfully", "data": serializer.data }, status=status.HTTP_201_CREATED)
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
            Method receives a http GET request and returns all subjects in the database
        """
        try:
            #Gets all subject objects 
            subjects = SubjectModel.objects.all()
            #Serializes the objects
            serializer = SubjectSerializer(subjects, many=True)
            #Returns the objects serialized and a sucess message
            return Response({"message": "All subjects returned", "data": serializer.data }, status=status.HTTP_200_OK)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation (e.args) and server side code
            return Response({"message": "Failed to get objects", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


