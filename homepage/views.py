from django.shortcuts import render


def home(request):
    return render(request, 'homepage/home.html')


def team(request):
    return render(request, 'homepage/team.html')


def contact(request):
    return render(request, 'homepage/contact.html')




