from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def home(request):
    return HttpResponse ('Olá, Django!')

def home_view(request):
    """
    Renderiza a página inicial com um template HTML, passando a data e hora atuais como contexto.
    """
    context = {
        'data_e_hora': datetime.now() # Variável Python que será acessível no template HTML
    }
    return render(request, 'meu_primeiro_html.html', context) # Renderiza o template especificado

def login(request):        
    usuario = 'Felipe'
    senha = '1234'
    if usuario == 'Felipe' and senha == '1234':
        resposta = "Login feito com sucesso!"
    else:
        resposta = "Acesso Negado - Tente Novamente"
    return HttpResponse(resposta)
