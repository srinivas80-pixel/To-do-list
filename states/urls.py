"""
URL configuration for states project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Himalayas.views import mountains,rivers,console,calculator,well,task,hero,heroine,delete_task,mark_completed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('s',mountains),
    path('a',rivers),
    path('i',console),
    path('l',calculator),
    path('@',well),
    path('k',task),
    path('$',hero),
    path('h',heroine),
    path('m',delete_task),
    path('put',mark_completed)
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
