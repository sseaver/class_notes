from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from app.forms import ContactForm

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = ContactForm()
        return context


class SendEmailView(FormView):
    success_url = reverse_lazy("index_view")
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
