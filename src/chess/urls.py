from django.urls import path

from chess.views import GameDetailsView

urlpatterns = [
    path('games/<int:pk>', GameDetailsView.as_view()),
]
