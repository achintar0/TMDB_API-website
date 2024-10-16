from django.views.generic import TemplateView
from datetime import datetime
from .api_services import TMDBClient
from django.shortcuts import render, redirect
import random

class TrendingMovies(TemplateView):
    template_name = 'movies/home.html'
    
    def get(self, request):
        movies = []
        trending_movie_dice = random.choice([1,2])
        if trending_movie_dice == 1:
            data = TMDBClient.fetch_day_trending_movies()
        else:
            data = TMDBClient.fetch_week_trending_movies()

        genre_map = TMDBClient.fetch_genre_ids()

        for movie in data:
            poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
            genre_names = [genre_map.get(genre_id, 'Unknown') for genre_id in movie.get('genre_ids', [])]
            
            movies.append({
                'title': movie['title'],
                'formatted_release_date': movie['release_date'],
                'vote_average': movie['vote_average'],
                'overview': movie['overview'],
                'poster_url': poster_url,
                'genres': genre_names,
            })

        for movie in movies:
            if movie['formatted_release_date']:
                release_date = datetime.strptime(movie['formatted_release_date'], "%Y-%m-%d")
                movie['formatted_release_date'] = release_date.strftime("%d %B %Y")

        context = {
            'movies': movies,
            'trending_movie_dice': trending_movie_dice
        }
        return self.render_to_response(context)

    
    