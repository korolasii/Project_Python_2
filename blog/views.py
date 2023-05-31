from django.shortcuts import render, get_object_or_404

from .models import Article
# Create your views here.
def details(request, id):
    article = Article.objects.get(id=id)
    print(article)
    return render(request, 'blog/details.html', {'article': article})


def random_article(request):
    article = Article.objects.order_by('?').first()
    return render(request, 'blog/details.html', {'article': article})

                         