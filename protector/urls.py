from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'protector'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='services'),
    path('about/', views.about, name='about')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)