
from django.urls import path
from .import views


urlpatterns = [  
    path('', views.main , name="home"),
    path('shah/<str:id>',views.haider,name="download")
]  