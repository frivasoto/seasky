from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView,DetailView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy

# Create your views here.
class Home1(TemplateView):
    template_name = 'base1.html'

