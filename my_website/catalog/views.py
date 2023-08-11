from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import all_card,CardForm
def my_index(request):
    cards = all_card.objects.all()
    columns = {
        "contend" : cards
 }
    return  render(request, 'index.html', context=columns)

def add_data(request):
    print(request.method)
    if request.method == 'POST':
        new_card = CardForm(request.POST)
        if new_card.is_valid():
            new_card.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/catalog/index/')
    else:
        new_card = CardForm()
    contend ={'form':CardForm()}
    return  render(request, 'add_data.html',contend)
def search(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)