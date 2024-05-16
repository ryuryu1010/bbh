from django.shortcuts import render
from django.http import HttpRespose

def index(request):
    return render(request, "index")
    return HttpRespose("ようこそ")