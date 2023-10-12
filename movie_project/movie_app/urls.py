from . import views
from django.urls import path
from .views import AllDirectors, AllActors, OneDirector, OneActor

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.show_directors),
    path('directors/<int:pk>', OneDirector.as_view(), name='one_dir'),
    path('actors/', views.show_actors),
    path('actors/<int:pk>', OneActor.as_view(), name='one_actor'),
    path('all_director', AllDirectors.as_view()),
    path('all_actors', AllActors.as_view())
]