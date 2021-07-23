from django.shortcuts import render
import json
from rest_framework.serializers  import Serializer
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class User_list(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Payment_account_list(APIView):

    def get_accounts(self, User_id):
        try: 
            return Payment_account.objects.filter(User_id_id=User_id)
        except Payment_account.DoesNotExist: 
            raise Http404


    def get(self, request, User_id):
        payment_account = self.get_accounts(User_id)
        serializer = Payment_accountSerializer(payment_account, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Payment_accountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Layout_List(APIView):

    def get(self, request):
        layouts = Layout.objects.all()
        serializer = LayoutSerializer(layouts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LayoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)