from typing_extensions import Required
from django.db import models
from django.db.models.deletion import CASCADE


class User(models.Model): 
    Name = models.CharField(max_length=50, required=True)
    Username = models.CharField(max_length=50, required=True)
    Password = models.CharField(max_length=50, required=True)
    Role = models.CharField(max_length=50, required=True)
    Phonenumber= models.PhoneNumberField(blank = True)


class Payment_account(models.Model):
    User_id = models.ForeignKey(User, on_delete=CASCADE, required = True)
    Address = models.CharField(max_length=100, required = True)
    Card_number = models.CharField(max_length=25, required = True)
    Exp_date = models.CharField(max_length=5, help_text="00/00", required = True)


class Layout(models.Model):
    Name = models.CharField(max_length = 50, required=True)
    Discription = models.CharField(max_length = 250, required=True)
    Price = models.FloatField()


class Services(models.Model):
    Name = models.CharField(max_length = 50, required=True)
    Discription = models.CharField(max_length = 250, required=True)
    Price = models.FloatField()


class Extras(models.Model):
    Name = models.CharField(max_length = 50, required=True)
    Discription = models.CharField(max_length = 250, required=True)
    Price = models.FloatField()


class Switches(models.Model):
    Name = models.CharField(max_length = 50, required=True)
    Discription = models.CharField(max_length = 250, required=True)
    Price = models.FloatField()
    Feel= models.CharField(max_length=20)
    Noise = models.CharField(max_length = 20)


class Shopping_cart(models.Model):
    User_id = models.ForeignKey(User, required = True)
    Build_id = models.ForeignKey(Build, required = True)


class Build(models.Model): 
    Layout_id = models.ForeignKey(Layout, required = True)
    Switch_id = models.ForeignKey(Switches, required = True)
    Services_id = models.ForeignKey(Services, required = True)
    Extras_id = models.ForeignKey(Extras, required=True)
