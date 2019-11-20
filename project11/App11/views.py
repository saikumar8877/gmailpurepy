from django.shortcuts import render
from django.core.mail import send_mail
from project11 import settings as sai
from django.shortcuts import HttpResponse

def registration(request):
    return render(request,"one.html")

def elogin(request):
    username=request.POST.get("uname")
    password=request.POST.get("pwd")

    if username=="Sathya" and password=="Tech":
         subject = "Thank you for logging Arvind Portal"
         message = "This is auto-generated mail"
         send_mail(subject, message, sai.EMAIL_HOST_USER, ["saikumar8877@gmail.com"])
         return render(request,"welcome.html")
    else:

        return render(request,"one.html" ,{"newmessage":"Invalid user details"})
def logout(request):
    return render(request,"one.html")




