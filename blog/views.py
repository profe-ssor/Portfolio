from django.shortcuts import render
from django.http import HttpResponse
from . models import Customers
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.



def inner_page(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data ={
                'name':name,
                'email':email,
                'subject':subject,
                'message':message
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['kyerematengcollins93@gmail.com'])
        
     return render(request, "blog/inner-page.html")

def handler404(request, exception):
    return HttpResponse("404: Page not Found")
   
