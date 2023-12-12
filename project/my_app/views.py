from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import Person
# Create your views here.

# Сначала производится проверка приходил ли POST запрос с
# переменной name и что-то передалось(то будет имя)
# , а иначе передаются формочки для вводда данных

def getData(request):
    tom = Person.objects.get_or_create(name="Tom", age=25, photo='bbv.jpg')
    mike = Person(name='Mike', age=15, photo='bebra.jpg')
    try:
        men = Person.objects.get(name='Mike2')
    except:
        str = 'Not Found'
    #mike.save() чтобы сохранить в бд
    people = Person.objects.all()
    return render(request, 'my_app/data.html', context={'data': people, 'str': str})



def index(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            return HttpResponse(f'Name: {name},{age},{email}')
        else:
            HttpResponse('Данные не валидны')
    else:
        form = UserForm()
        #form2 = UserForm2
        return render(request, 'my_app/ZADANIE.html', context={'form': form})