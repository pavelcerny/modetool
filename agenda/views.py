# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def agenda(request):
    return HttpResponse("Here will be the whole agenda (list of entries).")


def entry(request, entry_id):
    return HttpResponse("Here will be the entry (all template items, with corresponding entry item) ")


def template(request):
    return HttpResponse("here will be the template (list of template items)")