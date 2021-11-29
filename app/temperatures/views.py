from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Temperature


class TemperatureListView(ListView):
    model = Temperature
    paginate_by = 100


class TemperatureDetailView(DetailView):
    model = Temperature


class TemperatureCreateView(SuccessMessageMixin, CreateView):
    model = Temperature
    fields = "__all__"
    success_url = "/temperatures"
    success_message = "%(name)s was created successfully"


class TemperatureUpdateView(UpdateView):
    model = Temperature
    fields = "__all__"
    template_name_suffix = "_update_form"
