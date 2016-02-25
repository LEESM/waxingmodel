from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {'text': '말 적는 부분',}
    return render(request, 'index.html', context)