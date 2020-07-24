from django.urls import path
from .views import index, nosotros, servicios, certif, contact_success, store
from . import views
app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('nosotros', nosotros, name='nosotros'),
    path('servicios', servicios, name='servicios'),
    path('store', store, name='store'),
    path('contact_success', contact_success, name='contact_success')
]