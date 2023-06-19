from django.http import HttpResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
import os, environ
from rest_framework.parsers import JSONParser

def index(request):
 return HttpResponse("message")


@api_view(['POST'])
@parser_classes([JSONParser])
def hello_world(request, format=None):
    question= request.data['question']

    return Response({"message": question})