from django.shortcuts import render, HttpResponse

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html', {})