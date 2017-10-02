from django.db import models
from decimal import *
import re

# Create your models here.



class ProductManager(models.Manager):
	def validate(self, data):
		errors = []
		
		#brand
		if len(data['department']) == 0:
			errors.append("Product type can not be empty")
		
		#name
		if len(data['name']) < 8:
			errors.append("Name must be at least 8 characters")
			
		#price
		if len(data['price']) == 0:
			errors.append("Please specify a price")
		
		
		elif not re.match(r'^[0-9]+(.[0-9][0-9])?$',data['price']):
			errors.append("Price not valid. do not include the dollar sign, and if price is less that 1 enter a leading 0 ")
		
		
		elif Decimal(data['price']) < Decimal(0.01):
			errors.append("Price must be greater than 0")
		elif Decimal(data['price']) > Decimal(999.99):
			errors.append("We appologize, but we do not handle products priced greater than $999.99")
		
		#description
		if len(data['description']) == 0:
			errors.append("description can not be empty")
		if len(data['description']) > 50:
			errors.append("description can not be more than 50 characters")
		
		return errors
	
	def create_product(self, data):
		return self.create(
			department = data['department'],
			name = data['name'],
			price = float(data['price']),
			description = data['description'],
		)
	
	def update_product(self, data, id):
		product = self.filter(id=id).first()
		
		product.department = data['department']
		product.name = data['name']
		product.price = data['price']
		product.description = data['description']
		
		product.save()
		
	def delete_product(self, id):
		Product.objects.filter(id=id).first().delete()
		
		
class Product(models.Model):
	department = 	models.CharField(max_length=255)
	name = 			models.CharField(max_length=255)
	price = 		models.DecimalField(max_digits=6 ,decimal_places = 2)
	description = 	models.CharField(max_length=50)
	
	objects = ProductManager()
	
	created_at = 	models.DateField(auto_now_add=True)
	updated_at = 	models.DateField(auto_now=True)
	
	
	
# class StoreManager(models.Model):
	# def add_product(data):
		
		
		# pass

# class Store(models.Model):
	# products = models.ForeignKey(Product, related_name="store")
	
	# created_at = 	models.DateTimeField(auto_now_add=True)
	# updated_at = 	models.DateTimeField(auto_now=True)