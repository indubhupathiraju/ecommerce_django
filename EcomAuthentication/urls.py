from .views import RegistrationView, logoutUser, VerificationView,LoginView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate")
]