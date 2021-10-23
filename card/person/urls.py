from django.urls import path
from . import views
from .views import *


app_name = 'person'
urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', PersonListView.as_view(), name='persons'),
    path('person/<int:pk>', PersonDetailView.as_view(), name='person_detail'),
    path('add_person/', views.add_person, name='add_person'),
    path('createperson/', CreatePersonView.as_view(), name='createperson'),
    path('updateperson/<int:pk>/', UpdatePersonView.as_view(), name='updateperson'),
    path('deleteperson/<int:pk>/', PersonDeleteView.as_view(), name='deleteperson'),
]
