from django.urls import path

from . import views

urlpatterns=[
    path('calculator',views.home),
    path('add',views.add,name="add")
]