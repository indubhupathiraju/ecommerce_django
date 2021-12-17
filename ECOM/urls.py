from django.urls import path
from .views import ProceedToPayment
from . import views
urlpatterns = [
    path('', views.index, name='home-page'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("cart/", views.cart, name="cart"),
    path("cartView/products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="checkout"),
    path('payment/', ProceedToPayment.as_view(), name="payment"),
    path("update_item/", views.updateItem, name="update_item"),
    path("update_wishlist/", views.updateWishlist, name="update_wishlist"),
    path("cartView/", views.Catprod, name="cartView"),
    path("search/", views.Search, name="search"),
    path("search/products/<int:myid>", views.productView, name="search"),
    path("remove_prod/", views.RemoveProd, name="remove_prod"),
    path("remove_wishlist/",views.remove_wishlist, name="remove_wishlist"),
    path("order_completed/", views.CompleteOrder, name="completeOrder"),
    path("successful/", views.OrderSuccess, name="successful"),
    path("myorders/", views.MyOrders, name="myorders"),
    path('wishlist/',views.wishlist, name="wishlist"),
    path('shareProduct/<int:id>',views.shareProduct,name="shareProduct"),
]