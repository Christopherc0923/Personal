from django.urls import path
from . import views

# Assign appname for clarity
app_name = "pdf"

urlpatterns = [
    path('', views.pdf, name="pdf"),
] 