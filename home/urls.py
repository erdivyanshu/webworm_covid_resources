from django.contrib import admin
from django.urls import path, include
from home import views

#Django admin customization

admin.site.site_header = "Covid-Resources Portal"
admin.site.site_title = "Covid-19"
admin.site.index_title = "Welcome!In Covid-Resources Portal"


urlpatterns = [
    path('home', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('resources', views.resources, name="resources"),
    path('plasma', views.plasma, name="plasma"),
    path('vaccine', views.vaccine, name="vaccine"),
    path('gov', views.gov, name="gov"),
    path('symptoms',views.symptoms,name="symptoms"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
    path('contact_info', views.contact_info, name="contact_info"),
    path('search', views.search, name="search"),

]