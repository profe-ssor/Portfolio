from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


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
        send_mail(
            data["subject"],
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_RECIPIENT_EMAIL],
            fail_silently=False,
        )
        
     return render(request, "blog/inner-page.html")

def handler404(request, exception):
    return HttpResponse("404: Page not Found")
   
