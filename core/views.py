from django.shortcuts import render
from blog.models import *


def frontpage(request):
    articles = Article.objects.all()
    tags = Tag.objects.all()
    return render(request, 'core/frontpage.html', {'articles': articles, 'tags':tags})

def about(request):
    articles = Article.objects.all()
    personals = [
        {'name': 'Hilary Glenn', 'img_src': 'data:image/jpeg;base64,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', 'portfolio': '2020th 18 July'},
        {'name': 'Merryl Dorsey', 'img_src': 'https://cdn.fotosklad.ru/unsafe/06e87279ac7c4fcbb82d282b5ee9f4b2/image.jpg', 'portfolio': '2019 20 Septembre'},
        {'name': 'Jacob Bryant', 'img_src': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSb6vWITnGpMMkmxMQ-hXtma-7cGZeo_-dsaA&usqp=CAU', 'portfolio': '2023 11 Decembr'},
    ]
    return render(request, 'core/front_page_about.html', {'articles': articles,'persons': personals})

def pricing(request):
    articles = Article.objects.all()
    pricing = [
        {'price': '$0/mo', 'name': 'Free', 'bonus': [
            '10 users included',
            '2 GB of storage',
            'Email support',
            'Help center access'
        ]},
        {'price': '$15/mo', 'name': 'Pro', 'bonus': [
            '20 users included',
            '10 GB of storage',
            'Priority email support',
            'Help center access'
        ]},
        {'price': '$29/mo', 'name': 'Enterprise', 'bonus': [
            '30 users included',
            '15 GB of storage',
            'Phone and email support',
            'Help center access'
        ]}
    ]
    return render(request, 'core/front_page_pricing.html', {'articles': articles,'pricing': pricing})

def contacts(request):
    articles = Article.objects.all()
    contacts = {
        'name': 'Google',
        'address': '1600 Amphitheatre Pkwy, Mountain View, CA 94043, Соединенные Штаты',
        'email': 'google@gmail.com',
        'phone_number': '+16502530000',
        'map': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d24627.076708658762!2d-122.12277487656358!3d37.42320909833563!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fba02425dad8f%3A0x6c296c66619367e0!2z0JPRg9Cz0LvQv9C70LXQutGB!5e0!3m2!1sru!2sua!4v1685129023508!5m2!1sru!2sua"
    }
    return render(request, 'core/front_page_contacts.html', {'articles': articles,'contacts': contacts})