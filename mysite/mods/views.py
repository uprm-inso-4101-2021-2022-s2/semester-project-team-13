from django.shortcuts import render
from .models import Mod
from django.template import loader
from django.http import Http404, HttpResponse
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
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

        # template = loader.get_template('mods/dashboard.html')
        # return HttpResponse(template.render(None, request))