from django.urls import path
from .views import *

urlpatterns = [
    path('my-url/', my_views, name='my-view')  
]       