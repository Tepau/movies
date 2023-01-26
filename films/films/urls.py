"""films URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from filmsauth.views import SignUpView, SignInView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', SignInView.as_view(),name='connexion'),
    path('logout/', LogoutView.as_view(),name='deconnexion'),
    path('admin/', admin.site.urls),
    path('inscription/', SignUpView.as_view(), name='inscription' ),
    path('listing/', include('listing.urls', namespace='listing')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)