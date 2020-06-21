from django.urls import path
from .views import index, nosotros, servicios
from . import views
app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('nosotros', nosotros, name='nosotros'),
    path('servicios', servicios, name='servicios'),
]