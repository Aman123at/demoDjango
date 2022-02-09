from django.urls import re_path
from demoapp import views

urlpatterns = [
    re_path(r'^todos$',views.TodoApi),
    re_path(r'^todos/([0-9]+)$',views.TodoApi),
]
