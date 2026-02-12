from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('reasons/', views.reasons),
    path('secret/', views.password_page),
    path('final/', views.final),
    path('pirate/', views.onepiece),
]
