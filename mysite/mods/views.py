from django.shortcuts import render
from .models import Mod
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm, SearchForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView
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


def dashboard(request):
    return render(request, 'mods/dashboard.html')


def register(request):
    if request.method == "GET":
        return render(
            request, "mods/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            template = loader.get_template('mods/dashboard.html')
            return HttpResponse(template.render(None, request))


def modList(request):
    mod_list = Mod.objects.order_by('mod_title')[:5]
    template = loader.get_template('mods/modList.html')
    context = {
        'mod_list': mod_list,
    }
    return HttpResponse(template.render(context, request))

def gameList(request):
    mod_list = Mod.objects.order_by('mod_game')[:5]
    template = loader.get_template('mods/gameList.html')
    context = {
        'mod_list': mod_list,
    }
    return HttpResponse(template.render(context, request))




def modDetails(request, mod_id):
    try:
        mod = Mod.objects.get(pk=mod_id)
    except Mod.DoesNotExist:
        raise Http404("Mod does not exist")
    return render(request, 'mods/details.html', {'mod' : mod})


def About(request):
    template = loader.get_template('mods/About.html')
    return HttpResponse(template.render(None, request))


def search(request):
    if request.method == "GET":
        form = SearchForm()
        return render(
            request, "mods/search.html",
            {"form": SearchForm}
        )
    elif request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('mods/search_results.html')
        # mod_list = Mod.objects.filter_by(mod_game='Minecraft')[:5]
        # template = loader.get_template('mods/search_results.html')
        # context = {
        #     'mod_list': mod_list,
        # }
        # return HttpResponse(template.render(context, request))

