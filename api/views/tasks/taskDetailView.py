from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from api.serializers.task import TaskSerializer
from api.models.task import TaskModel
from api.models.student import StudentModel
from api.models.subject import SubjectModel
from rest_framework.exceptions import ValidationError



class TaskDetailView(APIView):
    """
        Retrieve, update or delete a task instance.    
    """

    def get_object(self, pk,model=TaskModel, entity="Task"):
        """
            Return a object by its primary key
        Args:
            pk(int): a value that represents the object pk
            model(class) : the model class
            entity(str): a string with the object type that will be retrieved
        """
        try:
            #Gets a object by its primary key
            return model.objects.get(pk=pk)
        except:
            #Raises a Http404  exception in case of not found
            raise Http404(f'`{entity} not found')
        
    def get_subjects(self, pk, model= SubjectModel, entity="Subjects"):
        """
            Return a list of  objects by its primary keys
        Args:
            pk(int): a value that represents the object pk
            model(class) : the model class
            entity(str): a string with the type of the object  that will be retrieved
        """
        try:
            #Gets a object by its primary key
            return model.objects.filter(pk__in = pk)
        except:
            #Raises a Http404  exception in case of not found
             raise Http404(f'`{entity} not found')
        
    def get(self, request, pk, format=None):
        """
            Returns a JSON of the object that contains the primary key handled by the url  

            Args:
            pk(int)  a value that represents the object pk

        """
        try:
            #Calls a function that gets a object by its pk
            task = self.get_object(pk)
            #Serializes the object
            serializer = TaskSerializer(task)
            #Returns the object found
            return Response({"message": "Task returned sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
        #Catches a exception raised in case of the object does not exist
        except Http404 as e:
            #Retuns a error message with the error explanation 
            return Response({"message": e.args}, status=status.HTTP_404_NOT_FOUND)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to get object", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def put (self, request, pk, format=None):
        """
           Update the object that contains the primary key handled by the url  

            Args:
            pk(int): a value that represents the object pk

        """
        try:
            #Calls the method that gets the student object by its pk
            student = self.get_object(request.data.get("student"), StudentModel, "Student")
            #Calls the method that gets the subjects object by its pk
            subjects = self.get_subjects(request.data.get("subjects"))
            #Calls the function that gets a object by its pk
            task = self.get_object(pk)
            #Serializes it and update it with the request data received
            serializer = TaskSerializer(task, data=request.data)
            #Validates the data object
            serializer.is_valid(raise_exception=True)
            #Saves the object in the database
            serializer.save(student=student, subjects=subjects)
            #Returns a sucess message and the object updated
            return Response({"message": "Task updated sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
        #Catches a exception raised in case of the object does not exist
        except Http404 as e:
            #Retuns a error message with the error explanation 
            return Response({"message": e.args}, status=status.HTTP_404_NOT_FOUND)
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
            pk(int): a value that represents the object pk

        """
        try:
            #Calls the function that gets a task by its pk
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
        except Http404 as e:
            #Retuns a error message with the error explanation 
            return Response({"message": e.args}, status=status.HTTP_404_NOT_FOUND)
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
            pk(int): a value that represents the object pk

        """
        try:
            #Calls the function that gets a student by its pk
            task = self.get_object(pk)
            #Serializes it 
            serializer = TaskSerializer(task).data
            #Deletes the object serialized
            task.delete()
            #Returns a sucess message and the object deleted
            return Response({"message": "Task deleted sucessfully", "data": serializer}, status=status.HTTP_200_OK)
        #Catches a exception raised in case of the object does not exist
        except Http404 as e:
            #Retuns a error message with the error explanation 
            return Response({"message": e.args}, status=status.HTTP_404_NOT_FOUND)
        #Abstracts all exception through python Exception class
        except Exception as e:
            #Retuns a error message with the error explanation 
            return Response({"message": "Failed to delete the object", "detail": e.args}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
