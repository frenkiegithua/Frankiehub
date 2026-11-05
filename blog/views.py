from django.shortcuts import render

from .models import Article


def article_list(request):
    articles = Article.objects.filter(status='published')
    return render(request, 'blog/article_list.html', {'articles': articles})
