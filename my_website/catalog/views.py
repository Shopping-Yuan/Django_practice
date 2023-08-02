from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import all_card
def my_index(request):
    cards = all_card.objects.all()
    columns = {
        "contend" : cards
 }
    return  render(request, 'index.html', context=columns)
