from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('blog-home', bloghome, name='blog-home'),
    path('price', price, name='price'),
    path('contact', contact, name='contact'),
    path('blog-single', blogsingle, name='blog-single'),
    path('elements', elements, name='elements'),
    path('portfolio', portfolio, name='portfolio'),
]
