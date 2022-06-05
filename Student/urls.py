from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('studentList/', views.studentList),
    path('studentProfile/', views.studentProfile, name = 'studentProfile'),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    path('studentSetting/',views.accountSettings, name = "studentSetting"),
    path('searchStudent/',views.searchStudent, name = 'searchStudent')
]
