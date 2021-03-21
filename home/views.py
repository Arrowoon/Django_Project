from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def bloghome(request):
    return render(request, 'blog-home.html')
def price(request):
    return render(request, 'price.html')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        data.save()
    return render(request, 'contact.html')
def blogsingle(request):
    return render(request, 'blog-single.html')
def elements(request):
    return render(request, 'elements.html')
def portfolio(request):
    return render(request, 'portfolio.html')