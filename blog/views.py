from django.shortcuts import render



def index(request):
    return render(request, "blog/index.html", {'title': 'Головна сторінка сайта'})


def about(request):
    return render(request, "blog/about.html")




