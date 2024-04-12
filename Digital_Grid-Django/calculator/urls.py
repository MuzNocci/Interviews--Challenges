from django.urls import path
from calculator import views



urlpatterns = [

    path("", views.view1, name="calculator"),
    #path("/", views.view2, name=""),

]