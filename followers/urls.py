from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollwerList.as_view()),
    path('followers/<int:pk>/', views.FollwerDetail.as_view()),
]