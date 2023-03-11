from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.landing, name="landing"),
    path('adminPage/', views.adminPage, name='adminPage'),
    path('contact/', views.contact, name="contact"),
    path('resume/', views.resume, name="resume"),
    path('ibm/', views.ibm, name="ibm"),
    path('publication/', views.publication, name="publication"),
    path('eid101/', views.eid101, name="eid101"),
    path('contact_submit/', views.contact_submit, name='contact_submit'),
    path('ml/', views.mlproj, name="mlproj"),
    path('cert/', views.cert, name="cert"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    #path('room/', views.room, name="room"),

    #Change when uploading full web
    path('todo/', views.todo, name="todo"),
    path('hac/', views.hac, name="hac"),
    path('utube/', views.utube, name="utube"),

]

