from django.urls import path
from . import views



urlpatterns= [
    path('',views.index,name = 'index'),
    path('registration/',views.registration,name='registration'),
    path('register/',views.register,name= 'register'),
    path('edit/<pk>',views.edit,name='edit'),
    path('delete/<pk>',views.delete,name='delete'),
]
