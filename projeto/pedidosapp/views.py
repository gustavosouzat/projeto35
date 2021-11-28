from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("<h1> aqui e o index<h1>")
    return render(request, 'pedidos/index.html')