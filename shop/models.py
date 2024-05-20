from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
class Product(models.Model):    
    name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products' )
    product_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='product_image/',null=True)
    about=models.CharField(max_length=1500,null=True)

    def __str__(self):
        return f'{self.name}'
    
class Air(models.Model):
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=1500)
    image=models.ImageField(upload_to='air_image/',null=True)
   
    def __str__(self):
        return f'{self.name}'
    

class Yol(models.Model):
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=1500)
    price=models.IntegerField()
    air=models.ForeignKey(Air,on_delete=models.CASCADE,related_name='yoll')
    image=models.ImageField(upload_to='yol_image/',null=True)
    def __str__(self):
        return f'{self.name}'
