from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from apps.corecode.views import IndexView

# Create your views here.


def wb_index(request):
    template = loader.get_template("wb_index.html")
    return HttpResponse(template.render())

def wb_about(request):
    template = loader.get_template("wb_about.html")
    return HttpResponse(template.render())

def wb_academics(request):
    template = loader.get_template("wb_academics.html")
    return HttpResponse(template.render())

def wb_admission(request):
    template = loader.get_template("wb_admission.html")
    return HttpResponse(template.render())

def wb_contact(request):
    template = loader.get_template("wb_contact.html")
    return HttpResponse(template.render())

def wb_facilities(request):
    template = loader.get_template("wb_facilities.html")
    return HttpResponse(template.render())

def wb_faculties(request):
    template = loader.get_template("wb_faculties.html")
    return HttpResponse(template.render())