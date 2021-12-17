from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
#from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import auth
from .utils import account_activation_token
from .models import *
# Create your views here.



class RegistrationView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'App/registration.html')


    def post(self, request):
        # GET USER DATA
        # VALIDATE
        # create a user account


        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirmpass = request.POST['password2']

        context = {
            'fieldValues': request.POST
        }
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'App/registration.html', context)


        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'App/registration.html', context)
                if confirmpass!=password:
                    messages.error(request, "Password didn't match")
                    return render(request, 'App/registration.html', context)


                user = User.objects.create_user(username=username,email=email)
                user.set_password(password)
                user.is_active = True
                user.save()
                # domain = get_current_site(request).domain
                # email_body = {
                #     'user': user,
                #     'domain': domain,
                #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                #     'token': account_activation_token.make_token(user),
                # }

                # link = reverse('activate', kwargs={
                #     'uidb64': email_body['uid'], 'token': email_body['token']})

                # email_subject = 'Activate your account'

                # activate_url =domain + link

                # email = EmailMessage(
                #     email_subject,
                #     'Hi ' + user.username + ', Please the link below to activate your account \n' + activate_url,
                #     'noreply@semycolon.com',
                #     [email],
                # )
                # email.send(fail_silently=False)
                messages.success(request, 'Account successfully created')
                # return render(request, 'App/login.html')
                return redirect('login')

        return render(request, 'App/login.html')


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'App/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            state=User.objects.get(username=username)
            user = auth.authenticate(username=username, password=password)
            print(state)


            if user:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('/')
            elif not state.is_active:
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'App/login.html')
            messages.error(
                request, 'Invalid username or password')
            return render(request, 'App/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'App/login.html')



def logoutUser(request):
    logout(request)
    return redirect('/')