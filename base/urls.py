from django.urls import path

from .views import (base, log_in
, product, about)

app_name = 'Main'

urlpatterns = [
    path('Homepage', base, name = 'homepage'),
    path('Login', log_in, name = 'login'),
    path('Product', product, name = 'product'),
    path('About', about, name = 'about')
]