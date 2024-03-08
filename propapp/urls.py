from django.contrib import admin
from django.urls import path
from propapp import views
urlpatterns = [
    path("",views.index, name= 'propapp'),
    path("contact",views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("search", views.search, name="search"),
    path("price", views.price, name="price"),
    path("<slug:plotid>", views.plotBrief, name ="plotBrief"),

]