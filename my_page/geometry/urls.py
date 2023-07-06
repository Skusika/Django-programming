from django.urls import path
from . import views
urlpatterns = [
    path('rectangle/<int:lengh>/<int:width>', views.get_rectangle_area, name='one'),
    path('square/<int:d>', views.get_square_area, name='two'),
    path('circle/<int:rad>', views.get_circle_area, name='three'),
    path('get_rectangle_area/<int:width>/<int:height>', views.rectangle),
    path('get_square_area/<int:width>', views.square),
    path('get_circle_area/<int:radius>', views.circle)
]