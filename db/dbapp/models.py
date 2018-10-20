from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

# class admindb(models.Model):
# 	randomtext=models.CharField(blank=False,max_length=1000)

# 	def __str__(self):
# 		return randomtext



class UserDetail(models.Model):
	
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	# user_type=models.CharField(choices=((1, _("OWNER")),(2, _("SHOP KEEPER")),default=1))
	user_type = models.IntegerField(choices=((1, ("owner")),(2, ("shopkeeper"))),default=1)
	address=models.CharField(blank=True,max_length=140)
	no_of_stores=models.IntegerField(blank=True,default=0)
	storeid=models.IntegerField(default=0)
	phone_no=models.CharField(max_length=13)

class Store(models.Model):
	name=models.CharField(blank=True,max_length=100)
	owner=models.ForeignKey(UserDetail,on_delete=models.CASCADE)


class Item(models.Model):
	name=models.CharField(blank=True,max_length=100)
	barcode=models.CharField(blank=True,max_length=100)
	quantity=models.IntegerField(default=0)
	price=models.IntegerField(default=0)
	store=models.ForeignKey(Store,on_delete=models.CASCADE)


class OrderShop(models.Model):#this is for the order distrubuter
	store=models.ForeignKey(Store,on_delete=models.CASCADE)
	name_shop=models.CharField(blank=True,max_length=100)
	address=models.CharField(blank=True,max_length=100)
	email=models.CharField(blank=True,max_length=100)
	shopkeeper_name=models.CharField(blank=True,max_length=100)
	phone_no=models.CharField(blank=True,default=0,max_length=100)



class Order_Item(models.Model):#this is for the customer side item table.
	order_shop=models.ForeignKey(OrderShop,on_delete=models.CASCADE)
	storeid=models.IntegerField(default=0)
	quantity=models.IntegerField(default=0)
	itemname=models.CharField(blank=True,max_length=100)




class Cart(models.Model):
	shopkeeper=models.CharField(max_length=100,blank=True)
	items=ArrayField(ArrayField(models.IntegerField(blank=True)),size=500)







