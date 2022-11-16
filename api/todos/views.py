from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Todo, Category
from .serializers import TodoSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get','post']

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    http_method_name = ['get','post']



# class TodoAPIView(APIView):

#     def get_object(self, pk):
#         try: 
#             return Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist:
#             raise Http404

#     # Read operation
#     def get(self, request, pk=None, format=None):
#         if pk:
#             data = self.get_object(pk)
#             serializer = TodoSerializer(data)
            
#         else:
#             data = Todo.objects.all()
#             serializer = TodoSerializer(data, many=True)

#         return Response(serializer.data)

#     # Create operation
#     def post(self, request, format=None):
#         print('you sent a post request')
#         data = request.data
#         serializer = TodoSerializer(data=data)

#         #Check data is valid
#         serializer.is_valid(raise_exception=True)

#         # Save the todo sent over
#         serializer.save()

#         # Inform the frontend
#         response = Response()

#         response.data = {
#             'message': 'Todo created successfully',
#             'data': serializer.data,
#         }

#         return response

#     # Put method
#     def put(self, request, pk=None, format=None):
#         print('UPDATE')
#         todo_to_update = Todo.objects.get(pk=pk)
#         data = request.data
#         serializer = TodoSerializer(instance = todo_to_update, data=data, partial=True)
        
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         response = Response()

#         response.data = {
#             'message': 'Todo Update Successfully',
#             'data': serializer.data
#         }

#         return response

#     # Delete method
    
#     def delete(self, request, pk, format=None):
#         remove = Todo.objects.get(pk=pk)

#         data = self.get_object(pk)
#         serializer = TodoSerializer(data)

#         response = Response()
        
#         response.data = {
#             'message': 'REMOVED OBJECT',
#             'data': serializer.data
#         }

#         remove.delete()

        

#         return response