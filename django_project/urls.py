"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from app import views

urlpatterns = [
    path('', views.home),
    path('busca/', views.busca),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('search/', views.search),
    path('clientarea/', views.clientarea),
    path('admin/', admin.site.urls),
    path('carrinho/', views.carrinho_de_compras, name='carrinho_de_compras'),
    path('minha-conta/', views.minha_conta, name='minha_conta'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('bisnaguinha/', views.bisnaguinha),
    path('product_list/', views.list_product, name='product_list'),
    path('recorrencia/', views.recorrencia),
    path('parabens-semanal/', views.parabensSemanal),
    path('parabens-quinzenal/', views.parabensQuinzenal),
    path('parabens-mensal/', views.parabensMensal),
    path('goiabinha/', views.goiabinha),
    path('rexona/', views.rexona),
    path('racao/', views.racao),
    path('nugget/', views.nugget),
    path('papel/', views.papel),
    path('bisnaguinha-panco/', views.bisnaguinha),
    path('biscoito-goiabinha/', views.goiabinha),
    path('desodorante-rexona/', views.rexona),
    path('racao-pedigree-adulto/', views.racao),
    path('nugget-sadia/', views.nugget),
    path('papel-higienico-neve/', views.papel),
    path('error/', views.error),
    path('add_to_cart/<item_id>/', views.add_to_cart),
    path('carrinho/remover/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('parabens-unico/', views.parabensUnico),
]
