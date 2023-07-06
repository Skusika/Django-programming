from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('type/', views.get_znak),
    path('type/<str:type_name>/', views.type, name='type_names'),
    path('<int:month>/<int:day>', views.get_info_by_date),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name')
]