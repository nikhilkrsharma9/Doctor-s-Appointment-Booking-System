from django.shortcuts import render
from django.db.models import Count,F

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from dproject1.models import *
import json
import urllib.request

# Create your views here.
from django.http import HttpResponse
def add(request):
    return render(request,'add.html')


def home1(request):
    return render(request,'home1.html')

def index(request):
    return render(request,'index.html')

def booking(request):
    b=appointment()
    b1=doctor()
    b.name=request.GET['name']
    b.email=request.GET['email']
    b.address=request.GET['address']
    b.phone=request.GET['phone']
    b.age=request.GET['age']
    b.option_gender=request.GET['option_gender']
    b.option_doctor=request.GET['option_doctor']
    b.fee=request.GET['fee']
    doc=request.GET['option_doctor']
    date=request.GET['date']
    x=appointment.objects.filter(option_doctor=doc,date=date).count()
    if x<10:
        b.save()
    else:
        return HttpResponse('Booking slots over')     
    b.date=request.GET['date']
    b.time=request.GET['time']
    b.reason=request.GET['reason']
    b.save()
    b1.save()
    return render(request,'home1.html')
    

def signup1(request):
    return render(request,'signup1.html')

def sign(request):
    a=userdata()
    a.name=request.GET['name']
    a.username=request.GET['username']
    a.email=request.GET['email']
    a.pwd=request.GET['pwd']
    a.repwd=request.GET['repwd']
    a.dob=request.GET['dob']
    a.chose1=request.GET['chose1']
    a.save()
    return render(request,'login.html')
    
def login(request):
    return render(request,'login.html')

def log(request):
    a=request.GET['first']
    b=request.GET['password']
    if userdata.objects.filter(username=a,pwd=b):
        #x=admin.objects.get(username=a)
        return render(request,'after_login.html')#,{'x':x})
    else:
        return render(request,'login.html')
    
def doctor_login(request):
    return render(request,'doctor_login.html')

def doctor_log(request):
    a=request.GET['first']
    d=request.GET['password']
    if appointment.objects.filter(option_doctor=a,doctor_pwd=d):
        x=doc.objects.get(doctor_name=a)
        return render(request,'doc_page.html',{'x':x})
    else:
        return HttpResponse('No Records Found')

def doctor_dash(request,name):
    u1=appointment.objects.get(option_doctor=name)
    q=appointment.objects.filter(option_doctor=name).count()
    if q<2:
        return render(request,'doctor_dash1.html',{'n':u1})
    else:
        return render(request,'doctor_dash.html',{'u1':u1})

def admin_dash(request):
    u1=appointment.objects.all()
    return render(request,'admin_dash.html',{'u1':u1})

def dele(request,id):
    u1=appointment.objects.get(id=id)
    u1.delete()
    return redirect('../admin_dash')
    
def edit(request,id):
    u1=appointment.objects.get(id=id)
    return render(request,'admin_dash_edit.html',{'u1':u1})

def dashedit(request,id):
    u1=appointment.objects.get(id=id)
    u1.option_doctor=request.GET['a1']
    u1.date=request.GET['a2']
    u1.time=request.GET['a3']
    u1.reason=request.GET['a4']
    u1.name=request.GET['a5']
    u1.save()
    return redirect('../admin_dash')

    
def admin_login(request):
    return render(request,'admin_login.html')

def admin_log(request):
    a=request.GET['first']
    b=request.GET['password']
    if admin.objects.filter(username=a,pwd=b):
        
        return render(request,'admin_page.html')
    else:
        return render(request,'admin_login.html')
    
def admin_signup(request):
    return render(request,'admin_signup.html')



def admin_sign(request):
    c=admin()
    c.name=request.GET['name']
    c.username=request.GET['username']
    c.email=request.GET['email']
    c.pwd=request.GET['pwd']
    c.repwd=request.GET['repwd']
    c.save()
    return render(request,'home1.html')

def after_login(request):
    return render(request,'after_login.html')

def admin_page(request):
    return render(request,'admin_page.html')
def docreg(request):
    return render(request,'docreg.html')
def docregcode(request):
    d=doc()
    d.doctor_name=request.GET['a1']
    d.email=request.GET['a2']
    d.pwd==request.GET['a3']
    d.save()
    return render(request,'docreg.html')

def user_account(request):
    a=userdata.objects.all()
    #x=userdata.objects.get(username=a)
    return render(request,'user_account.html')

#this is for about page
def About(request):
    return render(request,'About.html')

#this is doctor admin login 
def doctor_login(request):
    return render(request,'doctor_login.html')

#this is doctor after login page
def doc_page(request):
    return render(request,'doc_page.html')
