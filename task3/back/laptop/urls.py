from django.urls import path
from . import views
urlpatterns = [
 path('api/req/', views.hello_world),
]