from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Count, Avg, Value

# Create your views here.
def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('Hello'),
        int_field=Value(123),
        new_budget=F('budget') + 100
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    for movie in movies:
        movie.save()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


def show_directors(request):
    directors = Director.objects.order_by('last_name')
    for director in directors:
        director.save()
    return render(request, 'movie_app/directors.html', {
        'directors': directors
    })

def show_one_director(request, id_dir:int):
    director = get_object_or_404(Director, id=id_dir)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })

def show_actors(request):
    actors = Actor.objects.order_by('last_name')
    for actor in actors:
        actor.save()
    return render(request, 'movie_app/actors.html', {
        'actors': actors
    })

def show_one_actor(request, id_act:int):
    actor = get_object_or_404(Actor, id=id_act)
    return render(request, 'movie_app/one_actor.html', {
        'actor': actor
    })
