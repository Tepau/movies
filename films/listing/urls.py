from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import MovieListView


app_name = 'listing'
urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
