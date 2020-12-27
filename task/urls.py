from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="task-home"),
    path("newtask/",views.add_task,name="task-add")
]