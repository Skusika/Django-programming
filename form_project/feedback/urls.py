from django.contrib import admin
from django.urls import path
from . import views
from .views import index, done, update_feedback, FeedBackView, DoneView, FeedBackUpdateView, ListFeedBack, DetailFeedBack, FeedBackViewUpdate
urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
    path('detail/<int:pk>', DetailFeedBack.as_view()),
    path('detail/<int:pk>', FeedBackViewUpdate.as_view()),
    path('list', ListFeedBack.as_view())
]
