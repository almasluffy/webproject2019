from django.urls import  path
from api import views

urlpatterns = [

    path('login/', views.login),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view())

]