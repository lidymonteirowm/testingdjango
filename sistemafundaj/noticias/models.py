from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Noticias(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Rascunho'),
        ('published', 'Publicado'),
    )
    title = models.CharField(max_length=50, verbose_name='Título')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User)
    url = models.URLField(max_length=150, verbose_name='Link/URL')
    summary = models.TextField(max_length=100, verbose_name='Resumo')
    category = models.CharField(max_length=50, verbose_name='Categoria')
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name='Publicação')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Criação')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Atualização')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft', verbose_name='Status')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ('-publish',)