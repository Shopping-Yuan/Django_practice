from django.urls import path
from . import views


urlpatterns = [
    path("index/",views.my_index,name="index")
]