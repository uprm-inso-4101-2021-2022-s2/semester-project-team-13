from django.shortcuts import render
from .models import Mod
from django.template import loader
from django.http import Http404, HttpResponse
from django.http import HttpResponse
# Create your views here.
# from mysite.mods.models import Mod


def index(request):
    mod_list = Mod.objects.order_by('mod_title')[:5]
    template = loader.get_template('mods/index.html')
    context = {
        'mod_list': mod_list,
    }
    return HttpResponse(template.render(context, request))

def LoginForm(request):
    mod_list = Mod.objects.order_by('mod_title')[:5]
    template = loader.get_template('mods/LoginForm.html')
    return HttpResponse(template.render(None, request))