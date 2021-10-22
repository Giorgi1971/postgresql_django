from datetime import timezone
from django.utils import timezone
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Person
from .forms import PersonForm
# Create your views here.


def index(request):
    return render(request, 'person/index.html', {'time':timezone.now().date()})


# def persons(request):
#     person_list = Person.objects.all()
#     return render(request, 'person/person_list.html', {'person_list':person_list,
#         })


class PersonListView(ListView):
    model = Person


def add_person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            ff = form.save(commit=False)
            print(request.FILES)

            if 'photo' in request.FILES:
                ff.photo = request.FILES['photo']

            form.save(commit=True)
            return index(request)
        else:
            return render(request, 'person/add_person.html', {'form':form})
    return render(request, 'person/add_person.html', {'form':form})
