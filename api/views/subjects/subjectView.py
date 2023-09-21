from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.subject import SubjectSerializer
from api.models.subject import SubjectModel

class SubjectView(APIView):
    """
        List all students or create a new subject.
    """

    def post(self, request, format=None):
        """
            Method receives a http POST request and format type and create a subject object
        
        """
        try:
            #Get the data from the request and serialize it
            serializer = SubjectSerializer(data=request.data)
            #Validete the data serialized
            serializer.is_valid(raise_exception=True)
            #Save the new object in the database
            serializer.save()
            return Response({"message": "Subject created sucessfully", "data": serializer.data }, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "Failed to create"}, status=status.HTTP_400_BAD_REQUEST)
            
    
    def get(self, request, format=None):
        """
            Method receives a http POST request and format type and return all subject in the database
        """
        try:
            #Get all students objects 
            subjects = SubjectModel.objects.all()
            #Serializer the objects
            serializer = SubjectSerializer(subjects, many=True)
            # Return the objects serialized and a sucess message
            return Response({"message": "All subjects returned", "data": serializer.data }, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Failed"}, status=status.HTTP_400_BAD_REQUEST)


