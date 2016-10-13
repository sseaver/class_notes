from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView

from app.models import Chirp
from app.forms import ChirpForm
# Create your views here.


def index_view(request):
    if request.POST:
        instance = ChirpForm(request.POST)
        if instance.is_valid():
            instance.save()
    context = {
        "form": ChirpForm(),
        "all_chirps": Chirp.objects.all().order_by("-created")
    }
    return render(request, "index.html", context)


def about_view(request):

    return render(request, "about.html")


class ChirpView(ListView):
    template_name = "chirps.html"
    model = Chirp
