from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm, ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required()
def details(request, slug):
    article = get_object_or_404(Article, slug=slug, status='active')

def details(request, slug):
    article = get_object_or_404(Article, slug=slug, status='active')
    articles = Article.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return  redirect('details', slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog/details.html', {'articles': articles,'article': article, 'form': form})

def random_article(request):
    articles = Article.objects.all()
    article = Article.objects.filter(status='active').order_by('?').first()
    return render(request, 'blog/details.html', {'articles': articles,'article': article})

def articles_list(request):
    if not request.user.is_authenticated:
        return render(request, 'blog/error_login.html', {'title': "Помилка доступу"})
    articles = Article.objects.all()
    articles = Article.objects.filter(status='active')
    return render(request, 'blog/list.html', {'articles': articles,'articles': articles,'title': "Blog - головна сторінка"})

@login_required()
def articles_tag_list(request, tag):
    articles = Article.objects.filter(tags__name=tag, status='active')
    return render(request, 'blog/articles_tag_list.html', {'articles': articles, 'title': tag})

def articles_tag_list(request, tag):
    articles = Article.objects.all()
    articles = Article.objects.filter(tags__name=tag, status='active')
    return render(request, 'blog/articles_tag_list.html', {'articles': articles,'articles': articles, 'title': tag})

def articles_category_list(request, category):
    articles = Article.objects.all()
    searcharticles = Article.objects.filter(category__name=category, status='active')
    return render(request, 'blog/articles_category_list.html', {'articles': articles, 'searcharticles': searcharticles, 'title': category})

@login_required()
def search(request):
   articles = Article.objects.all()
   query = request.GET.get('query', '')
   searcharticles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(content_preview__icontains=query) | Q(tags__name__icontains=query) | Q(category__name__icontains=query), status='active')
   return render(request, 'blog/search.html', {'articles': articles, 'searcharticles': searcharticles, 'title': "Пошук по сайту", 'query': query})

@login_required()
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.add_message(request, messages.INFO, 'Cтаття створенна')
            return redirect('details', slug=article.slug)
    else:
        form = ArticleForm()
    return render(request, 'blog/create.html', {'form': form, 'title': "Створення статті"})

@login_required()
def update(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)

        if form.is_valid():
            article = form.save()
            messages.add_message(request, messages.INFO, 'Cтаття оновлена')
            return redirect('details', slug=article.slug)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/update.html', {'form': form, 'title': "Оновлення статті"})

@login_required()
def delete(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    article.delete()
    messages.add_message(request, messages.INFO, 'Cтаття видалена')
    return redirect('blog')