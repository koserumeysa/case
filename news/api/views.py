from rest_framework import status #request and response status
from rest_framework.response import Response #redirect, render
from rest_framework.decorators import api_view #decorator

from news.models import Essay
from news.api.serializers import EssaySerializer

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class EssayListCreateAPIView(APIView):
    def get(self, request):
        essays = Essay.objects.filter(isActive=True)
        serializer = EssaySerializer(essays, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EssaySerializer(data=request.data)
        serializer.is_valid()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class EssayDetailAPIView(APIView):
    def get_object(self, pk):
        essay_instance = get_object_or_404(Essay, pk=pk)
        return essay_instance

    def get(self, request, pk):
        essay = self.get_object(pk = pk)
        serializer = EssaySerializer(essay)
        return Response(serializer.data) 

    def put(self, request, pk):
        essay = self.get_object(pk = pk)
        serializer = EssaySerializer(essay, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        essay = self.get_object(pk = pk)
        essay.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








#Function Method
# @api_view(['GET','POST'])
# def essay_list_create_api_view(request):
#     if request.method == 'GET':
#         essays = Essay.objects.filter(isActive=True)
#         #This is a query object which includes objects.
#         serializer = EssaySerializer(essays, many=True)
#         #many=True is for serializing multiple objects.
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = EssaySerializer(data=request.data)
#         #request.data is for getting the data from the request.
#         serializer.is_valid()
#         #This is for checking whether the data is valid or not.
#         if serializer.is_valid():
#             serializer.save()
#             #This is for saving the data.
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#             #HTTP_201_CREATED is for creating the data.
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def essay_detail_api_view(request, pk):
#     essay_instance = Essay.objects.get(pk=pk)
#     #This is for getting the object with the primary key.
#     try:
#         essay_instance = Essay.objects.get(pk=pk)
#     except Essay.DoesNotExist:
#         return Response(
#             {'error':{
#             'code':404,
#             'message': f'Essay which has {{pk}} id was not found!'
#         }}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = EssaySerializer(essay_instance)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = EssaySerializer(essay_instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         essay_instance.delete()
#         return Response(
#             {'error':{
#             'code':204,
#             'message': f'Essay which has {{pk}} id was deleted!'
#         }},status=status.HTTP_204_NO_CONTENT)
    