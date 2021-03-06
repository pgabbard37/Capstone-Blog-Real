from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


def startpage(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/homepage.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})
