from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from api.serializers.task import TaskSerializer
from api.models.task import TaskModel
from api.models.student import StudentModel


class TaskDetailView(APIView):
    """
        Retrieve, update or delete a task instance.    
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
        
    def get(self, request, pk, format=None):
        """
            Returns a JSON of the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Get a student by its pk and serialize it
            task = self.get_object(pk, TaskModel)
            #Serialize the object
            serializer = TaskSerializer(task)
            # Return the object found
            return Response({"message": "Task return sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
        except:
            #In case of exception, generic message printed
            return Response({"message": "Task does not exist"}, status=status.HTTP_400_BAD_REQUEST)



    def put (self, request, pk, format=None):
        """
           Update the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Get a student by its pk
            task = self.get_object(pk, TaskModel)
            #Serielize it and update with the request data received
            serializer = TaskSerializer(task, data=request.data)
            #Validate the data object
            if serializer.is_valid():
                student = self.get_object(request.data.get("student"), StudentModel)
                serializer.save(student=student)
                #Return a sucess message and the object updated
                return Response({"message": "Task updated sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
            return Response({"message": "Failed", "detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:       
            #In case of exception, generic message printed
            return Response({"message": "Task could not be updated"}, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        """
           Partial update the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Get a student by its pk
            task = self.get_object(pk, TaskModel)
            #Serielize it and update with the request data received
            serializer = TaskSerializer(task, data=request.data, partial=True)
            #Validate the data object
            if serializer.is_valid():
                student = self.get_object(request.data.get("student"), StudentModel)
                serializer.save(student=student)
                #Return a sucess message and the object updated
                return Response({"message": "Task updated sucessfully", "data": serializer.data }, status=status.HTTP_200_OK)
            return Response({"message": "Failed", "detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:       
            #In case of exception, generic message printed
            return Response({"message": "Task could not be updated"}, status=status.HTTP_400_BAD_REQUEST)

          
    def delete(self, request, pk, format=None):
        """
           Delete the object that contains the primary key handled by the url  

            Args:
            pk : a value that represents the object pk

        """
        try:
            #Get a student by its pk
            subject = self.get_object(pk, TaskModel)
            #Serielize it and update with the request data received
            serializer = TaskSerializer(subject).data
            #Validate the data object
            subject.delete()
            #Return a sucess message and the object updated
            return Response({"message": "Task deleted sucessfully", "data": serializer}, status=status.HTTP_200_OK)
        except:       
            #In case of exception, generic message printed
            return Response({"message": "Task could not be deleted"}, status=status.HTTP_400_BAD_REQUEST)

