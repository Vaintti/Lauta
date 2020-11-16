from django.urls import path
from . import views

urlpatterns = [
    path('<str:uuid>/', views.thread, name='thread')
]