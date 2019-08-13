#! -.- coding: utf-8 -.-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


from django.contrib.auth import authenticate, login, logout



@login_required
def index(request):
    return render(request, 'index.html',)