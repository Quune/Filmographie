from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json as JSON

#//////////////////////////////////////////////////////////
#                GET
#//////////////////////////////////////////////////////////

@api_view(['GET'])
def listMovies(request, json):
    data = JSON.loads(json)
    print(data)
    pass

    #if request.method == 'GET':
    #   return Response()

    #elif request.method == 'POST':
    #    serializer = SnippetSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listSeries(request, json):
    pass

@api_view(['GET'])
def listHuman(request, json):
    pass

@api_view(['GET'])
def listMovies(request, json):
    pass

#//////////////////////////////////////////////////////////
#                   POST
#//////////////////////////////////////////////////////////


#//////////////////////////////////////////////////////////
#                   PUT
#//////////////////////////////////////////////////////////