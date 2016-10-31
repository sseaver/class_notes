from django.shortcuts import render
from django.views.generic import ListView, CreateView
from menu.models import Special
from django.urls import reverse_lazy


class SpecialListView(ListView):
    model = Special


class SpecialCreateView(CreateView):
    model = Special
    fields = ("title", "description")
    success_url = reverse_lazy('special_list_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_user = self.request.user
        return super().form_valid(form)
