from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def sistema(request):
    return render(request, 'sistema.html')