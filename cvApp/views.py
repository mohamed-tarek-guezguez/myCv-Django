from django.shortcuts import render, redirect
from .models import Certif, Contact
from .forms import contactForm

# Create your views here.
def homePage(request):
    return redirect(aboutPage)

def aboutPage(request):
    return render(request, 'about.html')

def resumePage(request):
    return render(request, 'resume.html')

def certifPage(request):
    certif = Certif.objects.all().order_by('-id')

    context = {
        'certif': certif,
    }

    return render(request, 'works.html', context)

def contactPage(request):

    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect(aboutPage)
    else:
        form = contactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact.html', context)