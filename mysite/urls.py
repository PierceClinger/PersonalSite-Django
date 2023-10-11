from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('email/', views.email, name='email'),
    path('email_submit/', views.email_submit, name='email_submit'),
    path('projects/', views.projects, name='projects'),
    path('chatbot/', views.chatbot, name='chatbot'),
]