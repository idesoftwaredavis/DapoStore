from django.shortcuts import render, redirect
from .models import ModelAdministrador, Product
from django.contrib.auth.models import User
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from passlib.hash import pbkdf2_sha256
from django.http import JsonResponse
from django.views.generic import TemplateView

def admin_login(request):
    form = AuthenticationForm()
    print("Loading.. ")
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)

            if user is not None:
                do_login(request,user)
                return redirect('managment:admin_home')
    return render(request, 'admin/login.html', {'form':form})


def admin_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        question = request.POST['question']
        answer = request.POST['answer']
        print(question)
        if question == '1':
            question = "¿Cual es tu banda favorita?"
        elif question == '2':
            question = "¿Objeto mas valioso para usted?"
        elif question == '3':
            question = "¿Nombre de su perro?"


        passwordEncrypt = pbkdf2_sha256.encrypt(password,rounds=12000, salt_size=32)
        model = ModelAdministrador.objects.create(username = username, password = passwordEncrypt, security_question = question, answer_question = answer)
        user = User.objects.create_user(username,email,password )
        user.is_staff = True
        user.is_superuser = True
        model.save()
        user.save()
        return redirect('managment:admin_login')
    return render(request, 'admin/admin-register.html')


def admin_home(request):
    if request.user.is_authenticated:
        return render(request, 'admin/home_admin.html', {})
    return redirect('managment:admin_login')

def admin_logout(request):
    # Finally session
    do_logout(request)
    # redirecto to index
    return redirect ('core:index')

#GET
def admin_products(request):
    product = Product.objects.all()
    ctx = {'model' : product}
    return render(request, 'admin/admin-products.html',ctx)
