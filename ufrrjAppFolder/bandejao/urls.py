from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:refeicaoID>/', views.detail, name='detail'),
]