from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('studentList/', views.studentList),
    path('studentProfile/', views.studentProfile),
]
