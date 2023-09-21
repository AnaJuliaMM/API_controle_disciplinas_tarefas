from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from api.serializers.subject import SubjectSerializer
from api.models.subject import SubjectModel

class SubjectDetailView(APIView):
    """
        Retrieve, update or delete a subject instance.    
    """

    def get_object(self, pk):
        """
            Return a object by its primary key
        Args:
            pk : a value that represents the object pk
        """
        try:
            return SubjectModel.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self, request, pk, format=None):
        """
            Returns a JSON of the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Get a student by its pk and serialize it
            subject = self.get_object(pk)
            #Serialize the object
            serializer = SubjectSerializer(subject)
            # Return the object found
            return Response({"message": "Subject return sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
        except:
            #In case of exception, generic message printed
            return Response({"message": "Subject does not exist"}, status=status.HTTP_400_BAD_REQUEST)



    def put (self, request, pk, format=None):
        """
           Update the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Get a student by its pk
            subject = self.get_object(pk)
            #Serielize it and update with the request data received
            serializer = SubjectSerializer(subject, data=request.data)
            #Validate the data object
            serializer.is_valid(raise_exception=True)
            serializer.save()
            #Return a sucess message and the object updated
            return Response({"message": "Subject updated sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
        except:       
            #In case of exception, generic message printed
            return Response({"message": "Subject could not be updated "}, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        """
           Partial update the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Get a student by its pk
            subject = self.get_object(pk)
            #Serielize it and update with the request data received
            serializer = SubjectSerializer(subject, data=request.data, partial=True)
            #Validate the data object
            serializer.is_valid(raise_exception=True)
            serializer.save()
            #Return a sucess message and the object updated
            return Response({"message": "Subject updated sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
        except:       
            #In case of exception, generic message printed
            return Response({"message": "Subject could not be updated"}, status=status.HTTP_400_BAD_REQUEST)

          
    def delete(self, request, pk, format=None):
        """
           Delete the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Get a student by its pk
            subject = self.get_object(pk)
            #Serielize it and update with the request data received
            serializer = SubjectSerializer(subject).data
            #Validate the data object
            subject.delete()
            #Return a sucess message and the object updated
            return Response({"message": "Subject deleted sucessfully", "data": serializer}, status=status.HTTP_200_OK)
        except:       
            #In case of exception, generic message printed
            return Response({"message": "Subject could not be deleted"}, status=status.HTTP_400_BAD_REQUEST)

