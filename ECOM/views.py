from django.shortcuts import render
from .models import *
from math import ceil
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views import View
from django.contrib import messages
import random


# Create your views here.

def shareProduct(request,id):
    user = request.user
    product = Product.objects.values('id')
    return render(request, 'App/shareProduct.html',{'id':product})

def index(request):
    user = request.user
    products = Product.objects.all()
    catprods=Product.objects.values('category','id')
    cats=Category.objects.all()

    if  user.is_authenticated:
        orderItem = CartItem.objects.filter(user=user)
        quantity=0
        for item in orderItem:
           quantity+=item.quantity
    else:
        quantity=0


    params = { 'product': products, 'quantity': quantity, 'cats':cats,}
    return render(request,'App/Homepage.html', params)
def about(request):
    return render(request,'App/about.html')
def contact(request):
    return render(request,"We are at contact")
def tracker(request):
    return render(request,'We are at tracker')
def cart(request):
    user = request.user
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    products = CartItem.objects.filter(user=user)
    quantity = 0
    for item in products:
        quantity += item.quantity
    Total=0
    for item in products:
        Total+=item.get_total
    return render(request, 'App/cart.html',{'OrderItem': products, 'Total':Total,'quantity':quantity, 'cats':cats})

def productView(request, myid):

    user = request.user
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    orderItem = CartItem.objects.filter(user=user)
    quantity=0
    for item in orderItem:
        quantity+=item.quantity
    product=Product.objects.filter(id=myid)
    return render(request, "App/prodview.html", {'product':product[0], 'quantity':quantity, 'cats':cats})

def checkout(request):
    user = request.user
    address= Address.objects.filter(user=user)
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    products = CartItem.objects.filter(user=user)
    quantity = 0
    for item in products:
        quantity += item.quantity
    Total = 0
    for item in products:
        Total += item.get_total
    return render(request, "App/checkout.html", {'OrderItem': products, 'Total':Total,'quantity':quantity, 'cats':cats, 'address':address})

def updateItem(request):
    print('in update_item')
    data = json.loads(request.body)
    user = request.user
    productId = data['productId']
    print('hi')
    print(productId)
    action = data['action']
    print(action)
    product = Product.objects.get(id=productId)
    orderItem, created = CartItem.objects.get_or_create(product=product,user=user)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item added now' , safe=False)

def updateWishlist(request):
    data = json.loads(request.body)
    user = request.user
    productId = data['productId']
    action = data['action']
    product = Product.objects.get(id=productId)
    wishlistItem, created = WishList.objects.get_or_create(product=product,user=user)
    wishlistItem.save()

    return JsonResponse('Item added' , safe=False)

def Catprod(request):
    user = request.user
    cat=request.GET
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    category = cat['category']
    orderItem = CartItem.objects.filter(user=user)
    quantity=0
    for item in orderItem:
        quantity+=item.quantity
    prod = Product.objects.filter(category=category)


    return render(request, 'App/products.html',{'prod': prod,'quantity': quantity,'category':category, 'cats':cats})

class ProceedToPayment(View):
    def get(self, request):
        return render(request, 'App/checkout.html')

    def post(self, request):
        user = request.user
        catprods = Product.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        products = CartItem.objects.filter(user=user)
        quantity = 0
        for item in products:
            quantity += item.quantity
        Total = 0
        for item in products:
            Total += item.get_total
        customer = request.POST['name']
        email = request.POST['email']
        street_address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zipcode']
        mobile = request.POST['mobile']
        if len(zip)!=6:
            messages.error(
                request, 'Invalid Zip code')
            return render(request, 'App/checkout.html',  {'OrderItem': products, 'Total':Total,'quantity':quantity})

        address, created = Address.objects.get_or_create(user=user, customer=customer,email=email, street_address=street_address, city=city, state=state, zip=zip, mobile=mobile)
        return render(request, 'App/checkout.html',  {'OrderItem': products, 'Total':Total,'quantity':quantity})


def CompleteOrder(request):
    data = json.loads(request.body)
    address_id=data['selectedValue']
    payment_mode= data['value']
    address = Address.objects.filter(id=address_id).get()
    shipping_address = ''
    shipping_address += address.street_address + ', \n' + address.city +', \n'+ address.state + ', \n' + str(address.zip)
    user= request.user
    products = CartItem.objects.filter(user=user)
    product=''
    for item in products:
        product += item.product.product_name + '  Quantity= ' + str(item.quantity) + ' price= ' + str(item.get_total) +'\n'
    Total = 0
    for item in products:
        Total += item.get_total
    product+= 'Total =' + str(Total)
    print(item.quantity)
    order_id=random.randint(100000,999999)
    for item in products:
        orders, created = OrderedItem.objects.get_or_create(product=item.product, quantity=item.quantity, user=user,Payment=payment_mode,orderID=order_id )

    order, created= Orders.objects.get_or_create(customer=user, shipping_address=shipping_address, product=product, Payment=payment_mode, orderID=order_id)
    CartItem.objects.filter(user=user).delete()
    return JsonResponse('Item added', safe=False)

def Search(request):
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    user = request.user
    products = CartItem.objects.filter(user=user)
    quantity = 0
    for item in products:
        quantity += item.quantity
    search = request.GET['search']
    post= Product.objects.filter(category__icontains=search)
    if post:
        return render(request, 'App/search.html', {'post':post, 'search':search})
    else:
        post = Product.objects.filter(product_name__icontains=search)
        return render(request, 'App/search.html', {'post': post,'search':search, 'quantity':quantity, 'cats':cats})


def RemoveProd(request):
    data = json.loads(request.body)
    prodID = data['productId']
    product = Product.objects.get(id=prodID)
    print(product)
    CartItem.objects.filter(product=product).delete()
    return JsonResponse('Item removed', safe=False)
def remove_wishlist(request):
    data = json.loads(request.body)
    prodID = data['productId']
    product = Product.objects.get(id=prodID)
    WishList.objects.filter(product=product).delete()
    return JsonResponse('Item deleted',safe=False)

def OrderSuccess(request):
    return render(request, 'App/ordersuccess.html')

def MyOrders(request):
    user=request.user
    products= OrderedItem.objects.filter(user=user)
    objects= CartItem.objects.filter(user=user)
    quantity=0
    for item in objects:
        quantity+=item.quantity
    return render(request, 'App/myorders.html' ,{'products':products,'quantity':quantity})


def wishlist(request):
    user = request.user
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    products = WishList.objects.filter(user=user)
    return render(request, 'App/wishlist.html',{'OrderItem': products, 'cats':cats})
