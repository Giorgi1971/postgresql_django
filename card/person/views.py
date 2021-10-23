"""
პირადობის მოწმობის მონაცემების შეტანა ბაზაში, კორექტირება, წაშლა. 
მონაცემები არაა User კლასთან დაკავშირებული.
"""
from datetime import timezone
from django.db.models import fields
from django.urls import reverse_lazy
from django.utils import timezone
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Person
from .forms import PersonForm
from django.views.generic import (CreateView, DeleteView, UpdateView, DetailView, ListView)


def index(request):
    return render(request, 'person/index.html', {'time':timezone.now().date()})


class PersonListView(ListView):
    model = Person


# ამ მეთოდით უფრო მარტივად ვასებთ, მეტი ავტომატიზაცია აქვს და ვალიდაცია
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


class CreatePersonView(CreateView):
    fields = '__all__'
    model = Person


class UpdatePersonView(UpdateView):
    fields = '__all__'
    model = Person


class PersonDetailView(DetailView):
    model = Person


# ეს არ შლის სურათს მედია ფაილიდან. გადასაწყვეტია ...
class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('person:persons')