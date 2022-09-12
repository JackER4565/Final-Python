"""Final URL Configuration

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
from django.contrib import admin
from django.urls import path
from App import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
    #path('', views.logout2, name="logout"),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('actuales/', views.actuales, name='actuales'),
    path('single_view/<string>', views.single_view, name="single_view"),
    path('vencidas/', views.vencidas, name='vencidas'),
    path('ganadores/', views.ganadores, name='ganadores'),
    path('FAQ/', views.faq, name='faq'), 
    path('acerca_de/', views.acerca_de, name='acerca_de'),
    #path("accounts/login/", name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.login2, name="login"),
    path('agregar_entrada/', views.agregar_entrada, name="agregar_entrada")
]

# add this lines
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)