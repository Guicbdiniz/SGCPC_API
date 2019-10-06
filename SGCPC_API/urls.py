"""SGCPC_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from SP_API.views import PesquisaViewSet, teste, InvestigadorViewSet, EquipeDeApoioViewSet, SaidaFinanceiraViewSet, \
    EntradaFinanceiraViewSet
from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pesquisas', PesquisaViewSet, basename='pesquisas')
router.register(r'investigadores', InvestigadorViewSet, basename='investigadores')
router.register(r'equipesdeapoio', EquipeDeApoioViewSet, basename='equipes de apoio')
router.register(r'entradafinanceira', EntradaFinanceiraViewSet, basename='entradas financeiras')
router.register(r'saidafinanceira', SaidaFinanceiraViewSet, basename='saidas financeiras')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'sgcpc/', include(router.urls)),
    url(r'teste', teste)
]
