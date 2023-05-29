from django.urls import path

from chess.views import GameDetailsView, PieceDetailsView, PieceMoveApiView

urlpatterns = [
    path('games/<int:pk>', GameDetailsView.as_view()),
    path('games/<int:pk>/pieces/<str:position>', PieceDetailsView.as_view()),
    path('games/<int:pk>/moves/<str:positions>', PieceMoveApiView.as_view()),
]
