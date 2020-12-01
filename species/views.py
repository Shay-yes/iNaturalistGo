from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *

def gallery_view(request):
    if request.method == 'GET':

        speciesList = Species.objects.all()
        return render(request, 'species/gallery.html', {'allSpecies' : speciesList})

def submit_view(request):

    form_class = SpeciesForm
    form = form_class(request.POST or None, request.FILES)
    #form.fields['user'].initial = request.user
    if request.method == 'POST':
        #form = SpeciesForm(request.POST, request.FILES)

        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            messages.success(request, "upload success")
            return redirect('home')

        else:
            form = SpeciesForm()

    return render(request, 'species/species_form.html', {'form' : form})


