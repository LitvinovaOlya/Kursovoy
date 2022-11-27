"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from content.views import *
from django.contrib.auth import urls
import content.views
from djangoProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('service/', service, name="service"),
    path('about_us/', about_us, name="about_us"),
    path('contact/', contact, name="contact"),
    path('delete_zayavka/<id_zayavka>', delete_zayavka, name='delete_zayavka'),
    path('update_zayavka/<id_zayavka>', update_zayavka, name='update_zayavka'),
    path('delete_vizajist/<id_vizajist>', delete_vizajist, name='delete_vizajist'),
    path('update_vizajist/<id_vizajist>', update_vizajist, name='update_vizajist'),
    path('add_vizajist/', add_vizajist, name='add_vizajist'),
    path('delete_makeup/<id_makeup>', delete_makeup, name='delete_makeup'),
    path('update_makeup/<id_makeup>', update_makeup, name='update_makeup'),
    path('add_makeup/', add_makeup, name='add_makeup'),
    path('delete_pricheski/<id_pricheski>', delete_pricheski, name='delete_pricheski'),
    path('update_pricheski/<id_pricheski>', update_pricheski, name='update_pricheski'),
    path('add_pricheski/', add_pricheski, name='add_pricheski'),
    path('accounts/', include('users.urls', namespace='users')),
    path('accounts/', include(urls)),
    path('adminka/', adminka, name="adminka"),
    path('admin_vizajist/', admin_vizajist, name='admin_vizajist'),
    path('admin_makeup/', admin_makeup, name='admin_makeup'),
    path('admin_pricheski/', admin_pricheski, name='admin_pricheski'),
    path('admin_kvalif/', admin_kvalif, name='admin_kvalif'),
    path('delete_kvalif/<id_kvalif>', delete_kvalif, name='delete_kvalif'),
    path('update_kvalif/<id_kvalif>', update_kvalif, name='update_kvalif'),
    path('add_kvalif/', add_kvalif, name='add_kvalif'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
