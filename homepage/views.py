from django.shortcuts import render

# from django.http import HttpResponse

def home(request):
    return render(request, 'homepage/home.html')

def team(request):
    return render(request, 'homepage/team.html')

def contact(request):
    return render(request, 'homepage/contact.html')