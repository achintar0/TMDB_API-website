from django.urls import path
from .views import TrendingMovies

urlpatterns = [
    path('', TrendingMovies.as_view(), name='home')
]
