from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_page, name='chat'),
    path('api/chat/', views.chatbot_api, name='chatbot_api'),
]
