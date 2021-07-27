from django.http import HttpResponse, Http404
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        ser = SnippetSerializer(snippets, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        ser = SnippetSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "POST"])
# def snippet_list(request, format=None):
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         ser = SnippetSerializer(snippets, many=True)
#         return Response(ser.data)

#     elif request.method == "POST":
#         ser = SnippetSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    # function to get objects from the model objects and check if it exists
    def get_objects(self, pk):
        try:
            return Snippet.objects.get(id=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_objects(pk)
        ser = SnippetSerializer(snippet)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        snippet = self.get_objects(pk)
        ser = SnippetSerializer(snippet, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = Snippet.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "PUT", "DELETE"])
# def snippet_detail(request, pk, format=None):
#     try:
#         snippet = Snippet.objects.get(id=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         ser = SnippetSerializer(snippet)
#         return Response(ser.data, status=status.HTTP_200_OK)

#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         ser = SnippetSerializer(data=data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
