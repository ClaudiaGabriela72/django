from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', index),
]

#path('', views.index, name='index')