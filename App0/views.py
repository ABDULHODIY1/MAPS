from django.shortcuts import render
from django.views.generic import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer
from rest_framework import generics
# Create your views here.
class Home(TemplateView):
    template_name = 'base.html'
class Mapd(TemplateView):
    template_name = 'index2.html'
class Map2Real(TemplateView):
    template_name = 'test.html'

class LocationList(APIView):
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
