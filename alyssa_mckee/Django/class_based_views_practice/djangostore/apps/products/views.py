from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .models import Product
from django.contrib import messages

def flasherrors(req, errors):
	for error in errors:
		messages.error(req, error)

# Create your views here.
class Stores(View):
	def get(self, req): #show storefront all items
		context = {
			"products": Product.objects.all()
		}
		
		return render(req, "products/storefront.html", context)
		
	def post(self, req): #add to store
		errors = Product.objects.validate(req.POST)
		if not errors:
			Product.objects.create_product(req.POST)
		else:
			flasherrors(req,errors)
		return redirect(reverse("store"))
	
class Products(View):
	def get(self, req, id): #show the item page
		print("get request")
		product = Product.objects.filter(id=id).first()
		if product:
			context = {
				"product": product,
			}
			return render(req, "products/product.html", context)
		return redirect(reverse("store"))
	
	def post(self, req, id): #process item edit/update
		print("patch request")
		product = Product.objects.filter(id=id).first()
		if product:
			errors = Product.objects.validate(req.POST)
			if errors:
				flasherrors(req,errors)
				return redirect(reverse("products", kwargs={"id": id}))
			
			Product.objects.update_product(req.POST, id)
			
		return redirect(reverse("store"))
		
def delete(req, id): #process item delete
	print("delete request")
	product = Product.objects.filter(id=id).first()
	if product:
		Product.objects.delete_product(id)
	return redirect(reverse("store"))


