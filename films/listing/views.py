from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Movie

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'

    def get_queryset(self):
        year = self.request.GET.get('year')
        qs = super().get_queryset()
        if year is not None:
            return qs.filter(date__year=year)
        return qs
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        years = [movie.date.year for movie in Movie.objects.all()]
        data['years'] = list(set(years))
        return data