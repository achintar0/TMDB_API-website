from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


class MoviesLogin(LoginView):
    template_name = 'accounts/login.html'

class MoviesLogout(View):
    template_name = 'movies/home.html'

    def get(self, request):
        logout(request)
        return redirect('home')
    
class MoviesRegister(View):
    template_name = 'accounts/register.html'

