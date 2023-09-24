from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from api.serializers.task import TaskSerializer
from api.models.task import TaskModel
from rest_framework.exceptions import ValidationError



class TaskDetailView(APIView):
    """
        Retrieve, update or delete a task instance.    
    """

    def get_object(self, pk):
        """
            Return a object by its primary key
        Args:
            pk : a value that represents the object pk
        """
        try:
            #Gets a object by its primary key
            return TaskModel.objects.get(pk=pk)
        except:
            #Raises a Http404  exception in case of not found
            raise Http404
        
    def get(self, request, pk, format=None):
        """
            Returns a JSON of the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Calls a function that gets a student by its pk
            task = self.get_object(pk)
            #Serializes the object
            serializer = TaskSerializer(task)
            #Returns the object found
            return Response({"message": "Task returned sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
        #Catches a exception raised in case of the object does not exist
        except Http404:
            #Retuns a error message with the error explanation 
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to get object", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def put (self, request, pk, format=None):
        """
           Update the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Calls the function that gets a student by its pk
            task = self.get_object(pk)
            #Serializes it and update it with the request data received
            serializer = TaskSerializer(task, data=request.data)
            #Validates the data object
            serializer.is_valid(raise_exception=True)
            #Saves the object in the database
            serializer.save()
            #Returns a sucess message and the object updated
            return Response({"message": "Task updated sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
        #Catches a exception raised in case of the object does not exist
        except Http404:
            #Retuns a error message with the error explanation 
            return Response({"message": "Task not  found"}, status=status.HTTP_404_NOT_FOUND)
        #Catches the error raised in the serializer validation
        except ValidationError as e:
            #Returns a dictionary with the exception name and its detail
            return Response({"message": "Validation error", "detail": e.args}, status=status.HTTP_400_BAD_REQUEST)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to update the object", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self, request, pk, format=None):
        """
           Partial update the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Calls the function that gets a student by its pk
            task = self.get_object(pk)
            #Serializes it and update it with the request data received
            serializer = TaskSerializer(task, data=request.data, partial=True)
            #Validates the data object
            serializer.is_valid(raise_exception=True)
            #Saves the object in the database
            serializer.save()
            #Returns a sucess message and the object updated
            return Response({"message": "Task updated sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
        #Catches a exception raised in case of the object does not exist
        except Http404:
            #Retuns a error message with the error explanation 
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        #Catches the error raised in the serializer validation
        except ValidationError as e:
            #Returns a dictionary with the exception name and its detail
            return Response({"message": "Validation error", "detail": e.args}, status=status.HTTP_400_BAD_REQUEST)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to update the object", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
          
    def delete(self, request, pk, format=None):
        """
           Delete the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Calls the function that gets a student by its pk
            subject = self.get_object(pk)
            #Serializes it 
            serializer = TaskSerializer(subject).data
            #Deletes the object serialized
            subject.delete()
            #Returns a sucess message and the object deleted
            return Response({"message": "Task deleted sucessfully", "data": serializer}, status=status.HTTP_200_OK)
        #Catches a exception raised in case of the object does not exist
        except Http404:
            #Retuns a error message with the error explanation 
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to delete the object", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
