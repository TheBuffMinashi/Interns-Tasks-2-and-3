from django.urls import path
from . import views
urlpatterns = [
 path("", views.index, name="index"),
 path('api/req/', views.hello_world),
]