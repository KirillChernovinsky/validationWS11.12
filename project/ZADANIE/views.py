from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.


peoples = []

def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email)
            #if email == 'User1@y.1' and password == '12345678':
            return render(request, 'ZADANIE/beforeentrance.html')

            # else:
            #     HttpResponse('отказано в доступе')
        else:
            HttpResponse('Данные не валидны')
    else:
        form = UserForm()
        #form2 = UserForm2
        return render(request, 'ZADANIE/entrance.html', context={'form': form})


def vhod(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            peoples.append(name)
            peoples.append(email)
            peoples.append(password)
            print(peoples)
            return render(request, 'ZADANIE/beforeregistr.html', context={'peoples':peoples[0]})
        else:
            HttpResponse('Данные не валидны')
    else:
        form = UserForm()
        #form2 = UserForm2
        return render(request, 'ZADANIE/ZADANIE.html', context={'form': form})
