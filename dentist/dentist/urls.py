
from django.contrib import admin
from django.urls import path,include
from website import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),

    ##### user related path##########################

    path('login/', views.Login, name ='login'),
    path('', auth.LogoutView.as_view(template_name ='home.html'), name ='logout'),
    path('register/', views.register, name ='register'),
    path('', include('django.contrib.auth.urls')),
]


