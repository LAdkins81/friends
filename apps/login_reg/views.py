from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
    return render(request, 'login_reg/index.html')

def login(request):
    return render(request, 'login_reg/login.html')

def authenticate(request):
    if request.method == 'POST':
        validemail = request.POST['form_email']
        validpass = request.POST['form_password']
        try:
            person = User.objects.get(email=validemail)
            personpassword = person.password
            if validpass == personpassword:
                request.session['name'] = person.alias
                request.session['id'] = person.id
                return redirect('friend:index')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid entry!')
                return redirect('login:login')
        except:
            messages.add_message(request, messages.ERROR, 'Your email and password have issues!')
            return redirect('login:login')

def register(request):
    return render(request, 'login_reg/register.html')

def create_employee(request):
    if request.method == 'POST':
        name = request.POST['form_name']
        alias = request.POST['form_alias']
        email = request.POST['form_email']
        password = request.POST['form_password']
        confirm = request.POST['form_confirm']
        dob = request.POST['form_dob']
        is_valid = True

        if EMAIL_REGEX.search(email) is None:
            messages.add_message(request, messages.ERROR, 'Email is not valid!')
            is_valid = False
        if len(password) < 8:
            messages.add_message(request, messages.ERROR, 'Your password must be at least 8 characters!')
            is_valid = False
        if password != confirm:
            messages.add_message(request, messages.ERROR, 'Passwords do not match!')
            is_valid = False
        if not is_valid:
            return redirect('login:register')
        else:
            try:
                user = User.objects.create(name=name, alias=alias, email=email, password=password, birthday=dob)
                request.session['id'] = user.id
                request.session['name'] = user.alias
                return redirect('friend:index')
            except:
                messages.add_message(request, messages.ERROR, 'Email already exists!')
                return redirect('login:register')
    else:
        return redirect('login:register')

def logout(request):
    request.session.clear()
    return redirect('login:index')
