from django.contrib import admin
from . import views
from django.urls import path

admin.site.site_header="YVIDH2K22"
admin.site.index_title ="Welcome to YIVDH2K22"
urlpatterns = [
    path("", views.home, name="home"),
    path('details/<int:pk>/', views.eventdetails.as_view(), name='details'),
    path('search',views.searching,name="search"),

]