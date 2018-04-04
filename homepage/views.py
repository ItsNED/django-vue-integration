from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from .models import Game


def index(request):
    games = Game.objects.all()
    return render(request, "homepage/index.html", {
        'games': games
    })

def games(request):
    games = serialize("json", Game.objects.all())
    return HttpResponse(games, content_type="application/json")
