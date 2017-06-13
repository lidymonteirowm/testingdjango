from django.shortcuts import render
from rest_framework import viewsets

from .models import Noticias
from .serializer import NoticiasSerializer


def noticia(request):
    noticias = Noticias.objects.all()
    context = {'noticias': noticias}
    return render(request, 'noticias/noticia.html', context)


class NoticiasViewSet(viewsets.ModelViewSet):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer