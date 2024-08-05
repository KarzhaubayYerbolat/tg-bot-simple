from django.urls import path
from . import views

urlpatterns = [
    path('getpost/', views.telegram_bot, name='getpost'),
    path('setwebhook/', views.setwebhook, name='setpost'),
]
