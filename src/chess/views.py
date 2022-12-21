from rest_framework.generics import RetrieveAPIView

from chess.models import Game
from chess.serializers import GameSerializer


class GameDetailsView(RetrieveAPIView):
    serializer_class = GameSerializer

    queryset = Game.objects.all()

    # def get(self, *args, **kw):
