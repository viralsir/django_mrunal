from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="task-home"),
    path("add/",views.add_task,name="task-add")
]