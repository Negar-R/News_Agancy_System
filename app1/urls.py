from django.urls import path
from .views import *

urlpatterns = [
    path('postNews' , postNews) , 
    path('getNews/<str:Date>' , getNews),
    path('putNews/<int:report_id>' , putNews),
    path('delNews/<int:iD>' , delNews)
]
