from django.urls import path
from blog import views

urlpatterns = [
    path("1", views.home, name="home"),
    path("2", views.page2, name="page2")
]