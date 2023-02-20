from django.urls import path
from . import views

# Assign appname for clarity
app_name = "heartattackclassification"

urlpatterns = [
    path('', views.heartattackclassification, name="heartattackclassification"),
    path('info/', views.info, name="info"),
    path('hac_submit', views.hac_submit, name="hac_submit"),
] 