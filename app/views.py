from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from .models import Produto

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from bs4 import BeautifulSoup
import requests
import decimal


def home(request):
    return render(request, "home.html")


def busca(request):
    List = Produto.objects.all()
    busca = request.GET.get('search') or ''
    if busca:
        List = Produto.objects.filter(nome__istartswith=busca)
    return render(request, 'busca.html', {'List': List, 'Searched': busca})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signin.html',
                          {'error_message': "Invalid email or password."})

    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/signin')
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def clientarea(request):
    return render(request, "clientarea.html")


def carrinho_de_compras(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] for item in cart.values())
    total_price_formatted = "{:.2f}".format(total_price)
    context = {'cart': cart, 'total_price': total_price_formatted}
    return render(request, 'carrinho.html', context)


def add_to_cart(request, item_id):
    item = Produto.objects.get(id=item_id)
    cart = request.session.get('cart', {})
    cart[item_id] = {
        'item_name': item.nome,
        'price': float(item.preco),
        'img': item.img.url
    }
    print(cart[item_id])
    request.session['cart'] = cart
    messages.success(request, f"{item.nome} foi adicionado ao carrinho!")
    return redirect('/carrinho')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        item_name = cart[str(item_id)]['item_name']
        del cart[str(item_id)]
        request.session['cart'] = cart
        messages.success(request, f"{item_name} foi removido do carrinho!")
    else:
        messages.error(request, "Item não encontrado no carrinho!")
    return redirect('/carrinho')


@login_required(redirect_field_name="/signin")
def minha_conta(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')

        user.username = username
        user.email = email
        user.first_name = first_name
        user.save()

        messages.success(request, 'Your account information has been updated.')
        return redirect('/minha-conta')

    cliente = request.user
    context = {'cliente': cliente}
    return render(request, 'contacliente.html', context)


def search(request):
    List = Produto.objects.all()
    busca = request.GET.get('search')
    if busca:
        List = Produto.objects.filter(nome=busca)
    return render(request, 'search.html', {'List': List})


def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Um email foi enviado com as instruções para redefinir sua senha.'
            )
            return redirect('login')
    else:
        form = PasswordResetForm()
    return render(request, 'reset_password.html', {'form': form})


#PÁGINAS QUE ESTÃO COM WEBSCRAPPING------------------------------------------------------------------------------


def bisnaguinha(request):
    produto = Produto.objects.get(id=1)
    url = 'https://www.superpaguemenos.com.br/pao-bisnaguinha-panco-300g/p?googleshopping=1'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find('span', class_='sale_price')

        if price_element:
            preco = price_element.text.strip()
            preco_texto = preco.replace('R$', '').replace(',', '.').strip()
            preco_decimal = decimal.Decimal(preco_texto)

            produto.preco = preco_decimal
            produto.save()
        else:
            preco = 'Preço não encontrado.'

        return render(request, 'bisnaguinha.html', {'preco': preco})
    else:
        return render(request, 'error.html',
                      {'message': 'Erro ao acessar o site de compras.'})


def goiabinha(request):
    produto = Produto.objects.get(id=2)
    url = 'https://www.superpaguemenos.com.br/biscoito-recheado-bauducco-maxi-goiabinha-30g/p'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find('span', class_='sale_price')

        if price_element:
            preco = price_element.text.strip()
            preco_texto = preco.replace('R$', '').replace(',', '.').strip()
            preco_decimal = decimal.Decimal(preco_texto)

            produto.preco = preco_decimal
            produto.save()
        else:
            preco = 'Preço não encontrado.'

        return render(request, 'goiabinha.html', {'preco': preco})
    else:
        return render(request, 'error.html',
                      {'message': 'Erro ao acessar o site de compras.'})


def rexona(request):
    produto = Produto.objects.get(id=3)
    url = 'https://www.superpaguemenos.com.br/desodorante-rexona-aerosol-masculino-active-150ml/p'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find('span', class_='sale_price')

        if price_element:
            preco = price_element.text.strip()
            preco_texto = preco.replace('R$', '').replace(',', '.').strip()
            preco_decimal = decimal.Decimal(preco_texto)

            produto.preco = preco_decimal
            produto.save()
        else:
            preco = 'Preço não encontrado.'

        return render(request, 'rexona.html', {'preco': preco})
    else:
        return render(request, 'error.html',
                      {'message': 'Erro ao acessar o site de compras.'})


def racao(request):
    produto = Produto.objects.get(id=4)
    url = 'https://www.superpaguemenos.com.br/racao-para-caes-pedigree-racas-pequenas-101kg/p'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find('span', class_='sale_price')

        if price_element:
            preco = price_element.text.strip()
            preco_texto = preco.replace('R$', '').replace(',', '.').strip()
            preco_decimal = decimal.Decimal(preco_texto)

            produto.preco = preco_decimal
            produto.save()
        else:
            preco = 'Preço não encontrado.'

        return render(request, 'racao.html', {'preco': preco})
    else:
        return render(request, 'error.html',
                      {'message': 'Erro ao acessar o site de compras.'})


def nugget(request):
    produto = Produto.objects.get(id=5)
    url = 'https://www.superpaguemenos.com.br/nuggets-de-frango-sadia-crocante-300g/p'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find('span', class_='sale_price')

        if price_element:
            preco = price_element.text.strip()
            preco_texto = preco.replace('R$', '').replace(',', '.').strip()
            preco_decimal = decimal.Decimal(preco_texto)

            produto.preco = preco_decimal
            produto.save()
        else:
            preco = 'Preço não encontrado.'

        return render(request, 'nugget.html', {'preco': preco})
    else:
        return render(request, 'error.html',
                      {'message': 'Erro ao acessar o site de compras.'})


def papel(request):
    produto = Produto.objects.get(id=6)
    url = 'https://www.superpaguemenos.com.br/papel-higienico-neve-folha-dupla-30m-leve-18-pague-16/p'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find('span', class_='sale_price')

        if price_element:
            preco = price_element.text.strip()
            preco_texto = preco.replace('R$', '').replace(',', '.').strip()
            preco_decimal = decimal.Decimal(preco_texto)

            produto.preco = preco_decimal
            produto.save()
        else:
            preco = 'Preço não encontrado.'

        return render(request, 'papel.html', {'preco': preco})
    else:
        return render(request, 'error.html',
                      {'message': 'Erro ao acessar o site de compras.'})


#---------------------------------------------------------------------------------------------------------------


def list_product(request):
    return render(request, 'list_product.html')


def recorrencia(request):
    return render(request, 'recorrencia.html')


def parabensSemanal(request):
    return render(request, "parabensSemanal.html")


def parabensQuinzenal(request):
    return render(request, "parabensQuinzenal.html")


def parabensMensal(request):
    return render(request, "parabensMensal.html")

def parabensUnico(request):
    return render(request, "parabensUnico.html")

def error(request):
    return render(request, "error.html")
