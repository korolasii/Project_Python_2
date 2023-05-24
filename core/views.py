from django.shortcuts import render

# Create your views here.
def frontpage(request):
    articles = [
        {'id': 1, 'title': 'First article', 'content': 'This is the first article'},
        {'id': 2, 'title': 'Second article', 'content': 'This is the second article'},
        {'id': 3, 'title': 'Third article', 'content': 'This is the third article'},
    ]
    return render(request, 'core/frontpage.html', {'articles': articles})