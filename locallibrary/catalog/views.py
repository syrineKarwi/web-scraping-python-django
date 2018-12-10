from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import RecherchForm

from urllib.request import urlopen as uRep
from bs4 import BeautifulSoup as soup


def index(request):

    if request.method == 'POST':

        form = RecherchForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['type']
            print("gggggggggggg",name)
            return HttpResponseRedirect('/thanks/')

    else:
        form = RecherchForm()

    return render(request, 'index.html', {'form': form})