from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', "Name", 'Username', "Password", "Role", "Phonenumber"] 


class Payment_accountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Payment_account
        fields = ['id', "Address", "Card_number", "Exp_date", "User"] 


class LayoutSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Layout
        fields = ['id', "Name", 'Discription', "Price"]


class ServicesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Services
        fields = ['id', "Name", 'Discription', "Price"] 

class ExtrasSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Extras
        fields = ['id', "Name", 'Discription', "Price"]      


class SwitchesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Switches
        fields = ['id', "Name", 'Discription', "Price", "Feel", "Noise"]

class Shopping_cartSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Shopping_cart
        fields = ['id', "User", "Build", "Price", "Build_name" ]

class BuildSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Build
        fields =  ['id', "Name", "Layout", "Switch", "Services", "Extras"]


class OrderSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Order
        fields = ['id', "User", "Build", "Price" ]
              