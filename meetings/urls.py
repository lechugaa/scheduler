from django.urls import path
from meetings import views


app_name = "meetings"

urlpatterns = [path("", views.index, name="index")]
