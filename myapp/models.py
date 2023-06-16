from django.db import models

# Create your models here.
class categorydb(models.Model):
    Category_Name=models.CharField(max_length=50,blank=True,null=True)
    image=models.ImageField(upload_to="categoryimage",blank=True,null=True)
    Description=models.CharField(max_length=50,blank=True,null=True)
class productdb(models.Model):
    category_Name=models.CharField(max_length=50,blank=True,null=True)
    Product_Name=models.CharField(max_length=50,blank=True,null=True)
    Pro_image=models.ImageField(upload_to="productimage",blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    Description=models.CharField(max_length=50,blank=True,null=True)
