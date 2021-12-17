from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

# Create your models here.
class Product(models.Model):
    product_image1= models.ImageField(upload_to='ECOM/images')
    product_image2 = models.ImageField(upload_to='ECOM/images', blank=True, null=True)
    product_image3 = models.ImageField(upload_to='ECOM/images', blank=True, null=True)
    product_image4 = models.ImageField(upload_to='ECOM/images', blank=True, null=True)
    product_image5 = models.ImageField(upload_to='ECOM/images', blank=True, null=True)
    product_name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=50 , default="")
    subcategory = models.CharField(max_length=50 , default="")
    desc = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity=models.IntegerField()

    def __str__(self):
        return self.product_name


class CartItem(models.Model):

        product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        quantity = models.IntegerField(default=0, null=True, blank=True)
        date_added = models.DateTimeField(auto_now_add=True,null=True)
        def __str__(self):
            return self.product.product_name
        @property
        def get_total(self):
            total = self.product.price * self.quantity
            return total

class WishList(models.Model):

        product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        date_added = models.DateTimeField(auto_now_add=True,null=True)
        def __str__(self):
            return self.product.product_name

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    street_address = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")
    zip = models.IntegerField( default="")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format +919999999999. Up to 14 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], max_length=17, unique=True, default='')

    def __str__(self):
        return self.customer

class Orders(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shipping_address= models.TextField( default="")
    product = models.TextField( default="")
    Payment = models.CharField(max_length=100,default='')
    Status = models.CharField(max_length=50,default='Pending')
    orderID = models.IntegerField(default=0)
    def __str__(self):
        return self.customer.username

class Category(models.Model):
    cat_name= models.CharField(max_length=100, default="")
    cat_image = models.ImageField(upload_to='ECOM/images')
    def __str__(self):
        return self.cat_name


class OrderedItem(models.Model):

        product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        quantity = models.IntegerField(default=0, null=True, blank=True)
        Payment = models.CharField(max_length=100, default='')
        Status = models.CharField(max_length=50, default='Pending')
        date_added = models.DateTimeField(auto_now_add=True,null=True)
        orderID= models.IntegerField(default=0)
        def __str__(self):
            return self.product.product_name
        @property
        def get_total(self):
            total = self.product.price * self.quantity
            return total