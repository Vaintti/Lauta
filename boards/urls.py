from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:url>/', views.board, name='board'),
    path('<str:url>/thread/', include('threads.urls'))
]