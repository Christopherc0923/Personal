from django.urls import path
from . import views

# Assign appname for clarity
app_name = "utube"

urlpatterns = [
    path('', views.utube, name="utube"),
    path('download_video/', views.download_video, name='download_video'),
    path('show_video/<str:video_title>/', views.show_video, name='show_video'),
] 