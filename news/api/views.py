from rest_framework import status #request and response status
from rest_framework.response import Response #redirect, render
from rest_framework.decorators import api_view #decorator

from news.models import Essay
from news.api.serializers import EssaySerializer

@api_view(['GET','POST'])
def essay_list_create_api_view(request):
    if request.method == 'GET':
        essays = Essay.objects.filter(isActive=True)
        #This is a query object which includes objects.
        serializer = EssaySerializer(essays, many=True)
        #many=True is for serializing multiple objects.
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EssaySerializer(data=request.data)
        #request.data is for getting the data from the request.
        serializer.is_valid()
        #This is for checking whether the data is valid or not.
        if serializer.is_valid():
            serializer.save()
            #This is for saving the data.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #HTTP_201_CREATED is for creating the data.
        return Response(status=status.HTTP_400_BAD_REQUEST)


