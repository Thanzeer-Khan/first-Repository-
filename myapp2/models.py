from django.db import models


#
class registrationdb(models.Model):
    User_Name=models.CharField(max_length=50,blank=True,null=True)
    Password=models.IntegerField(blank=True,null=True)
    Email_ID=models.EmailField(blank=True,null=True)
    Phone_Number=models.IntegerField(blank=True,null=True)
    Profile_Image=models.ImageField(blank=True,null=True)
class cartdb(models.Model):
    product_name=models.CharField(max_length=50,blank=True,null=True)
    description=models.CharField(max_length=50,blank=True,null=True)
    quantity=models.IntegerField(blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    total_price=models.IntegerField(blank=True,null=True)

class checkdb(models.Model):
    First_Name=models.CharField(max_length=50,blank=True,null=True)
    Second_Name=models.CharField(max_length=50,blank=True,null=True)
    Email=models.EmailField(blank=True,null=True)
    Phone_Number=models.IntegerField(blank=True,null=True)
    District=models.CharField(max_length=50,blank=True,null=True)


