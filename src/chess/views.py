from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from chess.controller import ChessController
from chess.models import Game
from chess.serializers import GameSerializer


class GameDetailsView(RetrieveAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class PieceDetailsView(RetrieveAPIView):
    queryset = Game.objects.all()

    def retrieve(self, request, *args, **kwargs):
        game = self.get_object()

        position = kwargs['position']
        position = tuple(map(int, position.split('-')))

        controller = ChessController(game)
        moves = controller.get_all_legal_moves_for_piece(position)

        return Response(moves)


class PieceMoveApiView(CreateAPIView):
    queryset = Game.objects.all()

    def create(self, request, *args, **kwargs):
        game = self.get_object()
        controller = ChessController(game)

        positions = kwargs['positions']
        p1, p2 = positions.split(';')

        p1 = tuple(map(int, p1.split('-')))
        p2 = tuple(map(int, p2.split('-')))

        controller.move_piece(p1, p2)

        return Response({'message': 'ok'})
