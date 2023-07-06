from django.urls import path
from . import views
urlpatterns = [
    path('<int:sign_days>', views.get_number_days),
    path('<str:sign_days>', views.get_info_about_sign_days, name='test'),
    # path('monday/', views.monday),
    # path('tuesday/', views.tuesday),
]