from django.shortcuts import render
from .models import Mod
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm, PublishForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.db.models import Q


def index(request):
    mod_list = Mod.objects.order_by('mod_title')[:5]
    template = loader.get_template('mods/index.html')
    context = {
        'mod_list': mod_list,
    }
    return HttpResponse(template.render(context, request))


def LoginForm(request):
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
    mod_list = Mod.objects.order_by('mod_title')
    template = loader.get_template('mods/modList.html')
    context = {
        'mod_list': mod_list,
    }
    return HttpResponse(template.render(context, request))


def gameList(request):
    game_list = Mod.objects.all().values('mod_game').distinct().order_by('mod_game')
    template = loader.get_template('mods/gameList.html')
    context = {
        'game_list': game_list,
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


# class SearchResults(ListView):
#     model = Mod
#     template_name = 'search.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         search_result = Mod.objects.filter(
#             Q(mod_title__icontains=query) | Q(mod_game__icontains=query)
#         )
#         return search_result

def search(request):
    if request.method == "GET":
        query = request.GET.get('search', None)
        # results = Mod.objects.filter(Q(mod_title__icontains=query) | Q(mod_author__icontains=query))

        game_list = Mod.objects.filter(mod_game=query)
        context = {
            'game_list': game_list,
        }
        template = loader.get_template('mods/search.html')
        return HttpResponse(template.render(context, request))


def publish(request):
    if request.method == "GET":
        return render(
            request, "mods/publish.html",
            {"form": PublishForm}
        )
    elif request.method == "POST":
        form = PublishForm(request.POST)
        if form.is_valid():
            form.save()
            template = loader.get_template('mods/modList.html')
            return HttpResponse(template.render(None, request))


# def discussion(request):
#