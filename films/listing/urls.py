from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.MovieListView.as_view(), name='movie_list'),

]