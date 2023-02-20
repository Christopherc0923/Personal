from django.urls import path
from . import views

# Assign appname for clarity
app_name = "expense"

urlpatterns = [
    path('', views.expense, name="expense"),
] 