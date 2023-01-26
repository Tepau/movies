from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import UserRegisterForm, MyAuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('movie-list')
    form_class = UserRegisterForm
    
    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
    
    def get_success_message(self, cleaned_data):
        username = cleaned_data['username'].capitalize()
        return f'Salut {username} ! Merci pour ton inscription'




class SignInView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = MyAuthenticationForm
    next_page = reverse_lazy('movie-list')

    def get_success_message(self, cleaned_data):
        return f'Salut {self.request.user.username} ! Content de te revoir'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('listing:movie-list')
        return super(SignInView, self).dispatch(request, *args, **kwargs)
    
