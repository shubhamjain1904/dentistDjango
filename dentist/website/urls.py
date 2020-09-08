

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('',views.home,name="home"),
    path('contact.html',views.contact,name="contact"),
    path('about.html',views.about,name="about"),
    path('pricing.html',views.pricing,name="pricing"),
    path('services.html',views.services,name="services"),
    path('openinghour.html',views.openinghour,name="openinghour"),
    path('report.html',views.report,name="report"),



    path('index.html', views.index, name ='index'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)