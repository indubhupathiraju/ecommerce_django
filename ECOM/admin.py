from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Address)
admin.site.register(Orders)
admin.site.register(Category)
admin.site.register(OrderedItem)
admin.site.register(WishList)