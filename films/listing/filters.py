import django_filters
from django_filters import FilterSet, ChoiceFilter
from .models import Movie
from django.contrib.auth.models import User

all_years = []
for movie in Movie.objects.all():
    if (movie.date.year, movie.date.year) not in all_years:
        all_years.append((movie.date.year, movie.date.year))

YEAR_CHOICES = tuple(all_years)
all_users = []
for user in User.objects.all():
    if (user.id, user.username) not in all_users:
        all_users.append((user.id, user.username))

USER_CHOICES = tuple(all_users)

class MovieFilter(FilterSet):
    year = ChoiceFilter(label='Année', field_name='date__year', choices=YEAR_CHOICES)
    user = ChoiceFilter(label='Utilisateur', field_name='user', choices=USER_CHOICES)

    class Meta:
        model = Movie
        fields = ['user', 'year']


    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super(MovieFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['user'].field.widget.attrs = ({'class': 'form-control'})
        self.filters['year'].field.widget.attrs = ({'class': 'form-control'})

