from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id', "Name", 'Username', "Password", "Role", "Phonenumber"] 


class Payment_accountSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Payment_account
        fields = ['id', "User_id", 'Address', "Card_number", "Exp_date"] 


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
        fields = ['id', "User_id", "Build_id" ]

class Buildserializer(serializers.ModelSerializer):
    class Meta: 
        model = Build
        fields =  ['id', 'Layout_id', 'Switch_id', "Services_id", "Extras_id"]
              