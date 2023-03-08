from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
import random
from .models import reg
from django.conf import settings
from django.core.mail import send_mail


def index(request):
        data = {'title':'Signup'}
        return render(request,'index.html',{'data':data})

def registration(request):
        if request.method == "POST":
                name = request.POST['na']
                city = request.POST['ci']
                email = request.POST['em']
                password = make_password(request.POST['pa'])
                if reg.objects.filter(Email=email).exists():
                     messages.error(request,'Email already exist')
                     return redirect('/')
                else:
                     reg.objects.create(Name=name,City=city,Email=email,Password=password)
                     messages.error(request,'create successfully')
                     return redirect('/')


def login(request):
        data = {'title':'Login'}
        return render(request,'login.html',{'data':data})

def log(request):
        if request.method == "POST":
                email = request.POST['em']
                password = request.POST['pa']
                if reg.objects.filter(Email=email).exists():
                        pas = reg.objects.get(Email=email)
                        psw = pas.Password 
                        if check_password(password,psw):
                             return HttpResponse('WELCOME')
                        else:
                             messages.error(request,'password incorrect')
                             return redirect('/login/')
                else:
                     messages.error(request,'Email not exist')
                     return redirect('/login/')


def forget(request):
        data = {'title':'forget'}
        return render(request,'forget.html',{'data':data})

def generate_otp(request):
        if request.method == "POST":
                email = request.POST['em']
                if reg.objects.filter(Email=email).exists():
                        n=random.random()
                        no=int(n*10000)
                        subject='otp'
                        message = str(no)
                        to = email
                        email_form = settings.EMAIL_HOST_USER
                        recipient_list = [to,]
                        send_mail(subject,message,email_form,recipient_list)
                        return render(request,'otpverify.html',{'code':no})     
                else:
                    messages.error(request,'email not valid')
                    return redirect('/forget/')

def otpverify(request):
        data = {'title':'otp verify'}
        return render(request,'otpverify.html',{'data':data})

def verify(request):
        if request.method=="POST":
                email = request.POST['em']
                if reg.objects.filter(Email=email).exists():
                        co = request.POST['co']
                        otp = request.POST['ot']
                        if co==otp:
                                return redirect('/update/')
                        else:
                                messages.error(request,'code invalid')
                                return redirect('/otpver/')
                else:
                        messages.error(request,'Email not exist')
                        return redirect('/otpver/')

def update(request):
        data = {'title':'update'}
        return render(request,'update.html',{'data':data})

def check(request):
        if request.method=="POST":
                email = request.POST['em']
                if reg.objects.filter(Email=email).exists():
                        pas = make_password(request.POST['pa'])
                        reg.objects.filter(Email=email).update(Password=pas) 
                        messages.success(request,'password set successfully')
                        return redirect('/update/')
                else:
                        messages.error(request,'Email not exist')
                        return redirect('/otpver/')