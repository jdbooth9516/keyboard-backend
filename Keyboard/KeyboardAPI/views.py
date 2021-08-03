from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from stripe.api_resources import line_item
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, response, HttpResponseRedirect
from django.http.response import JsonResponse
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

    def get_layout(self, pk):
        try: 
            return Layout.objects.get(pk=pk)
        except Layout.DoesNotExist:
            raise Http404


    def post(self, request):
        serializer = LayoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        layout = self.get_layout(pk)
        serializer = LayoutSerializer(layout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        

class Services_list(APIView):

    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)

    def get_service(self, pk):
        try: 
            return Services.objects.get(pk=pk)
        except Services.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        service = self.get_service(pk)
        serializer = ServicesSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class Extras_list(APIView):

    def get(self, request): 
        extras = Extras.objects.all()
        serializer = ExtrasSerializer(extras, many=True)
        return Response(serializer.data)

    def get_extra(self, pk):
        try: 
            return Extras.objects.get(pk=pk)
        except Extras.DoesNotExist:
            raise Http404

    def post(self, request): 
        serializer = ExtrasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        extra = self.get_extra(pk)
        serializer = ExtrasSerializer(extra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

            
class Switches_list(APIView):

    def get(self, request): 
        switches = Switches.objects.all()
        serializer = SwitchesSerializer(switches, many=True)
        return Response(serializer.data)

    def get_switch(self, pk):
        try: 
            return Switches.objects.get(pk=pk)
        except Switches.DoesNotExist:
            raise Http404

    def post(self, request): 
        serializer = SwitchesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        switch = self.get_switch(pk)
        serializer = SwitchesSerializer(switch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Build_list(APIView):
    def get_build(self, request, pk):
        try: 
            return Build.objects.filter(pk=pk)
        except Build.DoesNotExist:
            raise Http404

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

    def delete(self, request, pk):
        build = self.get_build(pk)
        build.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Shopping_cart_list(APIView):

    def get_user_cart(self, User_id):
        try: 
            return Shopping_cart.objects.filter(User_id=User_id)
        except Shopping_cart.DoesNotExist: 
            raise Http404

    def get_cart(self, pk):
        try: 
            return Shopping_cart.objects.filter(pk = pk)
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


    def delete(self,request, pk):
        cart = self.get_cart(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Payment(APIView): 
    stripe.api_key = "sk_test_51J09k7IegiEVwxhXjGVmOxHgTFqdKvLd18n3vnSTs13X8pv5AOy0QEvKyOGVsfDjiDad3OOIbu1lkm5pf3mfGHHI00shdRRtYE"
    def post(self, request):

        stripe.PaymentIntent.create(
            amount=request.data["amount"],
            currency='usd',
            payment_method_types=['card'],
        )   
        
        return Response()

class Orders(APIView): 

    def get(self, request): 
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)