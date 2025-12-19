
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('driverlogin/', views.driverlogin, name='driverlogin'),
    path('driverlogout/', views.driverlogout, name='driverlogout'),
    path('logout/', views.logout, name='logout'),
    path('markedroute/', views.markedroute, name='markedroute'),
    path('buslist/', views.buslist, name='buslist'),
    path('seat/<int:id>/', views.seat, name='seat'),
    path('getbusroute/<int:id>/', views.getbusroute, name='getbusroute'),
    path('booking/<int:id>/', views.booking, name='booking'),
    path('seatdetil/',views.saetdetail,name='saetdetail'),
]
