from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Article
# Create your views here.

def details(request, slug):
    article = get_object_or_404(Article, slug=slug, status='active')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return  redirect('details', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/details.html', {'article': article, 'form': form})

def random_article(request):
    article = Article.objects.filter(status='active').order_by('?').first()
    return render(request, 'blog/details.html', {'article': article})

def articles_list(request):
    articles = Article.objects.filter(status='active')
    return render(request, 'blog/list.html', {'articles': articles,'title': "Blog - головна сторінка"})

def articles_tag_list(request, tag):
    articles = Article.objects.filter(tags__name=tag, status='active')
    return render(request, 'blog/articles_tag_list.html', {'articles': articles, 'title': tag})

def articles_category_list(request, category):
    articles = Article.objects.filter(category__name=category, status='active')
    return render(request, 'blog/articles_category_list.html', {'articles': articles, 'title': category})

def search(request):
   query = request.GET.get('query', '')
   articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(content_preview__icontains=query) | Q(tags__name__icontains=query) | Q(category__name__icontains=query), status='active')
   return render(request, 'blog/search.html', {'articles': articles, 'title': "Пошук по сайту", 'query': query})
