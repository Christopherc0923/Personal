from django.urls import path
from . import views

# Assign appname for clarity
app_name = "stock"


urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
]