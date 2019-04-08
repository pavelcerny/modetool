# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
from rest_framework import generics

from agenda.form import NewEntryForm, NewTemplateItemForm
from agenda.models import Entry, TemplateItem, EntryItem
from agenda.serializers import EntrySerializer


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
    e = Entry.objects.get(pk=entry_id)
    template_item_list = TemplateItem.objects.all()
    entry_item_list = EntryItem.objects.filter(entry=e)
    context = {
        'entry': e,
        'template_item_list': template_item_list,
        'entry_item_list': entry_item_list,
    }

    return render(request, 'agenda/entry.html', context)
    # return HttpResponse("Here will be the entry (all template items, with corresponding entry item) ")


def delete_entry(request, entry_id):
    e = get_object_or_404(Entry, pk=entry_id)
    e.delete()

    return agenda(request)


def template(request):
    return HttpResponse("here will be the template (list of template items)")


def delete_template_item(request, template_item_id):
    ti = get_object_or_404(TemplateItem, pk=template_item_id)
    ti.delete()

    return todolist(request)


def todolist(request):
    # load data
    entry_list = Entry.objects.all()
    field_list = TemplateItem.objects.all()


    # prepare row labels
    row_label_array = []
    for t in field_list:
        row_label_array.append(t)
    heigth = len(row_label_array)

    # prepare column labels
    column_label_array = []
    for e in entry_list:
        column_label_array.append(e)
    width = len(column_label_array)

    # prepare all columns
    columns_array = [None] * width

    # go through every column
    for c_id in range(0, width):
        # prepare each single column

        # row_array = [None] * row_len
        row_array = [False] * heigth
        column_label = column_label_array[c_id]
        value_list = EntryItem.objects.filter(entry=column_label)

        # iterate rows
        for r_id in range(0, heigth):
            row_label = row_label_array[r_id]
            for value in value_list:
                if (row_label.id == value.id):
                    # row_array[r_id] = value.value
                    row_array[r_id] = True
                    break

        columns_array[c_id] = row_array


    # go through every
    rows_array = [[False for x in range(width)] for y in range(heigth)]
    for r_id in range(0, heigth):
        for c_id in range(0, width):
            rows_array[r_id][c_id] = columns_array[c_id][r_id]






    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewTemplateItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            ti = TemplateItem()
            name_from_form = form.cleaned_data.get('item_name')
            ti.label = name_from_form
            ti.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/todolist')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewTemplateItemForm()

    # pass the data to the template
    context = {
        'row_labels': row_label_array,
        'column_labels' : column_label_array,
        'rows_array': rows_array,
        'form': form,
    }

    return render(request, 'agenda/todolist.html', context)


# REST API


class EntryList(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
