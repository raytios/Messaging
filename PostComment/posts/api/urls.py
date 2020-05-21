from .views import MessageReadUpdate, MessageListAPIView, MessageCreate

from django.contrib import admin
from django.urls import path, include, re_path

app_name = 'post'

urlpatterns = [
    path('', MessageListAPIView.as_view(), name='message-list'),
    path('create/', MessageCreate.as_view(), name='message-create'),
    path('<int:Collaborate_Messaging_A00_Rec>/', MessageReadUpdate.as_view(), name='message-read'),
    #path('module/<int:pk>/', ModuleRead.as_view(), name='module-read'),
    #path('contact/<int:pk>/', ContactRead.as_view(), name='contact-read'),
]