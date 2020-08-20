from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('ABOUT',views.ABOUT,name="ABOUT"),
    path('CONTACT',views.CONTACT,name="CONTACT"),
]