from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
import environ

def index(request):
 return HttpResponse("message")


@api_view()
def hello_world(request):
  
    return Response({"message": "hello_world"})