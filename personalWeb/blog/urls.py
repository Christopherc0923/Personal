from django.urls import path
from . import views

# Assign appname for clarity
app_name = "blog"

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<int:blog_id>/', views.detail, name = 'detail'),
] 