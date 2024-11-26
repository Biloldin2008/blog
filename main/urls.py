from django.urls import path
from .views import *
urlpatterns = [
    path('about/',About),
    path('blog-details/',Blogdetails),
    path('blog/',Blog),
    path('contact/',Contact),
    path('index/',Index),
    path('project-details/',Projectdetails),
    path('projects/',Projects),
    path('service-details/',Servicedetails),
    path('services/',Services),
    path('starter-page/',Starterpage),
    path("send/",Send)
]