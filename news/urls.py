from django.urls import path
from news import views

urlpatterns = [
    path('news/', views.ChronicleList.as_view()),
    path('news/<int:pk>/', views.ChronicleDetail.as_view()),
]