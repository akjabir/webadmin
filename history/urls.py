from .import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<str:nam>', views.service),
    path('<str:name>/<str:nam>/', views.single_post),
    path('data-search/', views.data_search),
    path('privacy/', views.Privacy),
    path('aboutus/', views.Aboutus),
    path('term/', views.Term),
    path('contact/', views.Contact)
]