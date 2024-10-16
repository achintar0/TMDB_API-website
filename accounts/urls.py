from django.urls import path
from .views import MoviesLogin, MoviesLogout, MoviesRegister

urlpatterns = [
    path('login/', MoviesLogin.as_view(), name='login'),
    path('logout/', MoviesLogout.as_view(), name='logout'),
    path('register/', MoviesRegister.as_view(), name='register')
]
