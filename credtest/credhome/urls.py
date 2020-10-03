from django.urls import path
from .import views

urlpatterns = [
    path('', views.Homeview, name="home"),
    #path('', Homeview.as_view(), name="home"),
]