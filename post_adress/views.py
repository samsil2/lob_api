from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Address
from .serializers import AddressSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# @api_view(['GET'])
# def apiOverview(request):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer(queryset, many=True)
#     return Response(serializer_class.data)


@api_view(['GET'])
def getAPI(request, pk):
    queryset = Address.objects.get(id=pk)
    serializer_class = AddressSerializer(queryset, many=False)
    return Response(serializer_class.data)


@api_view(['POST'])
def insertAPI(request):
    serializer_class = AddressSerializer(data=request.data)

    if serializer_class.is_valid():
        serializer_class.save()

    return Response(serializer_class.data)


@api_view(['POST'])
def updateAPI(request, pk):
    queryset = Address.objects.get(id=pk)
    serializer_class = AddressSerializer(instance=queryset, data=request.data)

    if serializer_class.is_valid():
        serializer_class.save()

    return Response(serializer_class.data)


@api_view(['DELETE'])
def deleteAPI(request, pk):
    queryset = Address.objects.get(id=pk)
    queryset.delete()

    return Response('Item succsesfully delete!')


class ApiOverview(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['line1', 'line2', 'city', 'state', 'zip']

#API URL
# API Overview http://127.0.0.1:8000/api/
# INSERT http://127.0.0.1:8000/api/post/
# Get http://127.0.0.1:8000/api/get/2/ [id]
# Update http://127.0.0.1:8000/api/update/4/ [id]
# delete http://127.0.0.1:8000/api/delete/9/ [id]
# Search-> http://127.0.0.1:8000/api/?search=sev [text]