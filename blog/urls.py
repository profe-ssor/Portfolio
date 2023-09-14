from django.urls import path
from . import views


urlpatterns = [

    path('', views.inner_page, name="inner-page"),
]