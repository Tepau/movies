from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Movie

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'