from django.http import HttpResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(["GET", "POST"])
def snippet_list(request, format=None):
    if request.method == "GET":
        snippets = Snippet.objects.all()
        ser = SnippetSerializer(snippets, many=True)
        return Response(ser.data)

    elif request.method == "POST":
        ser = SnippetSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    try:
        snippet = Snippet.objects.get(id=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        ser = SnippetSerializer(snippet)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        ser = SnippetSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
