from django.shortcuts import render
from .models import Register,Enquiry,News
from .forms import regform,logform,Enquiryform,Newsletter
from django.http.response import HttpResponse

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from email.mime.image import MIMEImage
# from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
import json

from django.db.models import Q
from django.http import Http404
from django.http import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def admin2(request):
    return render(request, 'admin2.html',{'g':g})

def author(request):
    return render(request, 'author.html')

def jobs(request):
    return render(request, 'jobs.html')

def newsletter(request):
    return render(request, 'newsletter.html')


def register(request):
    if request.method == "POST":
        fform=regform(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
          
            data=Register(
                name=name,
                email=email,
                password=password
                )
            data.save()
            fform=regform()
            fdata = Register.objects.all()
            return render(request,'index.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = regform()
        fdata = Register.objects.all()
    return render(request, 'index.html',{'fform': fform,'fdata': fdata})

def login(request):
    if request.method=="POST":
        lform=logform(request.POST)
        if lform.is_valid():
            name=request.POST.get('name')
            password=request.POST.get('password')
            data=Register(
                name=name,
                password=password
                )
            g=data.name

            uname=Register.objects.filter(name=name)
            pwd=Register.objects.filter(password=password)

            if uname and pwd:
                return render(request, 'author.html',{'g':g})
            else:
                return render(request, '404.html')
        else:
            return render(request, '404.html')
    else:
        lform=logform()
        return render(request, 'index.html',{'lform': lform})


def Enquiryview(request):
    if request.method == "POST":
        fform=Enquiryform(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            jobtype=request.POST.get('jobtype')
            data=Enquiry(
                name=name,
                email=email,
                phone=phone,
                jobtype=jobtype
                )
            data.save()
            fform=Enquiryform()
            fdata = Enquiry.objects.all()
            return render(request,'admin2.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = Enquiryform()
        fdata = Enquiry.objects.all()
    return render(request, 'admin2.html',{'fform': fform,'fdata': fdata})


def newsletter2(request):
    email=request.POST.get('a8')
    f=News(Email=email)
    f.save()
    # img_data = open("courses.png", 'rb').read()
    # img = MIMEImage(img_data)
    subject, from_email,recipient_list = 'IT consultant service updates', 'settings.EMAIL_HOST_USER',[f.Email]
    text_content = 'This is an important message.'
    html_content = '<h3><p>Thank you for Subscribing 😃 ... you will get notifications as soon as possible 😃 </p></h3>'
    msg = EmailMultiAlternatives(subject, text_content, from_email,recipient_list)
    msg.attach_alternative(html_content, "text/html")
    # msg.attach(img)
    msg.send()

    return render(request,'newsletter.html')



