from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import ContactForm

def home(request):
    return render(request, 'homepage/home.html')

def team(request):
    return render(request, 'homepage/team.html')


# form logic
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'homepage/contact.html', {'form': form})
