from django.urls import path
from .views import index
from . import views
app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
]