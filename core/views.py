from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer


class TestView(APIView):
    def get(self, req, *args, **kwargs):
        qs = Customer.objects.all()
        serializer = CustomerSerializer(qs, many=True)
        return Response(serializer.data)

        return Response(data)

    def post(self, req, *args, **kwargs):
        serializer = CustomerSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
