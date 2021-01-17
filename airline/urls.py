from django.urls import path
from . import  views

urlpatterns=[
    path("",views.home,name="ariline-home"),
    path("info/<int:flight_id>",views.flight_info,name="flight_info")
]