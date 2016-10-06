from django.shortcuts import render
# from django.http import HttpResponse
import datetime
from record_store.models import Song


def index_view(request):
    context = {
        "my_name": "Sam the Man",
        "now": datetime.datetime.now(),
        "all_songs": Song.objects.all()
    }
    return render(request, "index.html", context)
    # return HttpResponse("I love web programming")
