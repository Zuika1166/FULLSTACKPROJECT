from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# def id(request):
#     return render(request, 'playground/main.html', {})


# def home(request):
#     return HttpResponse(1)

# request -> response
# request handler
# action

# ul.Top_Menu
def say_hello(request):
    return render(request, 'playground/main.html', {})


def home(request):
    return render(request, 'playground/home.html', {})


def about(request):
    return render(request, 'playground/about.html', {})


def login(request):
    return render(request, 'playground/login.html', {})


def singin(request):
    return render(request, 'playground/singin.html', {})


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'playground/portfolio.html', context=context)
