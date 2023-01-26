from django.urls import reverse_lazy
from .models import Movie
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import MovieFilter


class MovieListView(LoginRequiredMixin, FilterView):
    login_url = reverse_lazy('connexion')
    model = Movie
    template_name = 'movie_list.html'
    filterset_class = MovieFilter
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        years = [movie.date.year for movie in self.get_queryset()]
        data['years'] = list(set(years))
        return data