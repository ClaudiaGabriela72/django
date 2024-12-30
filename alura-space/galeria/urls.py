from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', views.index, name='index'),
    #path('', index),
]