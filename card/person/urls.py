from django.urls import path
from . import views
from .views import PersonListView


app_name = 'person'
urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', PersonListView.as_view(), name='persons'),
    path('add_person/', views.add_person, name='add_person'),
]
