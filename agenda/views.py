# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from agenda.form import NewEntryForm
from agenda.models import Entry


def agenda(request):
    # load entry items
    entry_list = Entry.objects.all()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewEntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            e = Entry()
            name_from_form = form.cleaned_data.get('entry_name')
            e.name = name_from_form
            e.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewEntryForm()

    # pass the data to the template
    context = {
        'entry_list': entry_list,
        'form': form
    }

    return render(request, 'agenda/agenda.html', context)

def entry(request, entry_id):
    return HttpResponse("Here will be the entry (all template items, with corresponding entry item) ")


def template(request):
    return HttpResponse("here will be the template (list of template items)")