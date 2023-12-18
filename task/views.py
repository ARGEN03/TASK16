from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET'])
def my_views(request):
    queryset = PersonalData.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    return Response(serializer.data)