from rest_framework import status #request and response status
from rest_framework.response import Response #redirect, render
from rest_framework.decorators import api_view #decorator

from news.models import Essay
from news.api.serializers import EssaySerializer

@api_view(['GET'])
def essay_list_create_api_view(request):
    if request.method == 'GET':
        essays = Essay.objects.filter(isActive=True)
        #This is a query object which includes objects.
        serializer = EssaySerializer(essays, many=True)
        #many=True is for serializing multiple objects.
        return Response(serializer.data)


