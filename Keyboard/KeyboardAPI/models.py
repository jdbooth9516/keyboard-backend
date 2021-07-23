from django.db import models
from django.db.models.deletion import CASCADE




class User(models.Model): 
    Name = models.CharField(max_length=50, blank=False)
    Username = models.CharField(max_length=50, blank=False)
    Password = models.CharField(max_length=50, blank=False)
    Role = models.CharField(max_length=50, blank=False)
    Phonenumber= models.CharField(max_length=20, blank = True)


class Payment_account(models.Model):
    User_id = models.ForeignKey(User, on_delete=CASCADE, blank = False)
    Address = models.CharField(max_length=100, blank = False)
    Card_number = models.CharField(max_length=25, blank = False)
    Exp_date = models.CharField(max_length=5, help_text="00/00", blank = False)


class Layout(models.Model):
    Name = models.CharField(max_length = 50, blank=False)
    Discription = models.CharField(max_length = 250, blank=False)
    Price = models.FloatField()


class Services(models.Model):
    Name = models.CharField(max_length = 50, blank=False)
    Discription = models.CharField(max_length = 250, blank=False)
    Price = models.FloatField()


class Extras(models.Model):
    Name = models.CharField(max_length = 50, blank=False)
    Discription = models.CharField(max_length = 250, blank=False)
    Price = models.FloatField()


class Switches(models.Model):
    Name = models.CharField(max_length = 50, blank=False)
    Discription = models.CharField(max_length = 250, blank=False)
    Price = models.FloatField()
    Feel= models.CharField(max_length=20)
    Noise = models.CharField(max_length = 20)


class Build(models.Model): 
    Layout_id = models.ForeignKey(Layout, on_delete=CASCADE, blank = False)
    Switch_id = models.ForeignKey(Switches, on_delete=CASCADE, blank = False)
    Services_id = models.ForeignKey(Services, on_delete=CASCADE, blank = False)
    Extras_id = models.ForeignKey(Extras, on_delete=CASCADE, blank=False)

class Shopping_cart(models.Model):
    User_id = models.ForeignKey(User, on_delete=CASCADE, blank = False)
    Build_id = models.ForeignKey(Build, on_delete=CASCADE, blank = False)