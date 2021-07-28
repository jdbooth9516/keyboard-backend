from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, response
import stripe

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

class Login(APIView):

    def get_users(self):
        users = list(User.objects.all().values())
        return users

    def post(self, request):
        users = self.get_users()
        
        print(users)
        for user in users: 
            print(user)
            print(request.data['Username'])
            if request.data['Username'] == user['Username'] and request.data['Password'] == user['Password']:
                print("logged in")
                return Response(user)


class Payment_account_list(APIView):

    def get_accounts(self, User_id):
        try: 
            return Payment_account.objects.filter(User_id=User_id)
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

class Services_list(APIView):

    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class Extras_list(APIView):

    def get(self, request): 
        extras = Extras.objects.all()
        serializer = ExtrasSerializer(extras, many=True)
        return Response(serializer.data)

    def post(self, request): 
        serializer = ExtrasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            
class Switches_list(APIView):

    def get(self, request): 
        switches = Switches.objects.all()
        serializer = SwitchesSerializer(switches, many=True)
        return Response(serializer.data)

    def post(self, request): 
        serializer = SwitchesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Build_list(APIView):

    def get(self, request): 
        builds = Build.objects.all()
        serializer = BuildSerializer(builds, many=True)
        return Response(serializer.data)

    def post(self, request): 
        buildserializer = BuildSerializer(data=request.data)
        if buildserializer.is_valid():
            buildserializer.save()
            return Response(buildserializer.data, status=status.HTTP_201_CREATED)
        return Response(buildserializer.data, status=status.HTTP_400_BAD_REQUEST)

class Shopping_cart_list(APIView):

    def get_user_cart(self, User_id):
        try: 
            return Shopping_cart.objects.filter(User_id=User_id)
        except Shopping_cart.DoesNotExist: 
            raise Http404


    def get(self, request, User_id):
        shopping_cart = self.get_user_cart(User_id)
        serializer = Shopping_cartSerializer(shopping_cart, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Shopping_cartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class Payment(APIView): 

    def post(self, request):
        stripe.api_key = "sk_test_51J09k7IegiEVwxhXjGVmOxHgTFqdKvLd18n3vnSTs13X8pv5AOy0QEvKyOGVsfDjiDad3OOIbu1lkm5pf3mfGHHI00shdRRtYE"
        print(request.data)

        stripe.PaymentIntent.create(
            amount= request.data['amount'],
            currency='usd',
            payment_method_types=['card'],
            receipt_email='jboothwebdev@gmail.com'
        )

        return Response()