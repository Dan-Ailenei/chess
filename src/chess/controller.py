from itertools import chain

from chess.maxtrix import get_box_positions
from chess.models import Position, Team, Game


class ChessController:
    """
    promote pawns
    """

    def __init__(self, game: Game):
        self.game = game

    def move_piece(self, piece_position: Position, to_position: Position):

        if self.is_move_legal(piece_position, to_position) is False:
            raise ValueError('Move is not legal')

        new_table = self.game.table.move_piece(piece_position, to_position)
        oponent_team = Team.get_oponent(self.game.team_to_play)

        if self._is_mate(new_table, oponent_team):
            self.finish_game(self.game.team_to_play)
        else:
            self.game.team_to_play = oponent_team
            self.game.table = new_table

    def is_move_legal(self, piece_position, to_position):
        piece = self.game.table.get_piece(piece_position)
        if piece is None:
            return False

        legal_moves = self._get_all_legal_moves_for_piece(self.game.table, piece_position)

        return to_position in legal_moves

    def _get_all_legal_moves_for_piece(self, table, piece_position, filter_moves_that_lead_to_check=True):
        piece = table.get_piece(piece_position)

        possible_moves = piece.get_moves(piece_position, self.game.table)

        if filter_moves_that_lead_to_check:
            possible_moves = self._filter_moves_that_lead_to_check(piece_position, possible_moves)

        return possible_moves

    def _is_in_check(self, table, team):

        king_position = table.get_king_position(team)

        all_pieces_moves_of_oponents = self._get_all_pieces_moves_of_team(table, Team.get_oponent(team), filter_moves_that_lead_to_check=False)
        in_check = king_position in chain(*all_pieces_moves_of_oponents.values())

        return in_check

    def _is_mate(self, table, team):
        if self._is_in_check(table, team):
            king_position = table.get_king_position(team)
            all_pieces_moves_of_oponents = self._get_all_pieces_moves_of_team(table, Team.get_oponent(team), filter_moves_that_lead_to_check=False)
            box_positions = get_box_positions(king_position)

            king_can_not_move = all(
                position in chain(*all_pieces_moves_of_oponents.values()) or
                table.get_piece(position) is not None
                for position in box_positions
            )
            
            if king_can_not_move is False:
                return False

            all_pieces_moves_of_current_team = self._get_all_pieces_moves_of_team(table, team)
            team_has_blocking_or_removing_check_moves = bool(list(chain(*all_pieces_moves_of_current_team.values()))) is False
            return team_has_blocking_or_removing_check_moves

        return False

    def _get_all_pieces_moves_of_team(self, table, team, filter_moves_that_lead_to_check=True) -> dict[Position, list[Position]]:
        all_pieces_moves_of_team = {}

        for piece_position in table.get_piece_positions(team):
            legal_moves = self._get_all_legal_moves_for_piece(table, piece_position, filter_moves_that_lead_to_check=filter_moves_that_lead_to_check)
            all_pieces_moves_of_team[piece_position] = legal_moves

        return all_pieces_moves_of_team

    def _filter_moves_that_lead_to_check(self, piece_position, possible_moves):
        playing_team = self.game.team_to_play

        legal_moves = []
        for move in possible_moves:
            table = self.game.table.move_piece(piece_position, move)
            if self._is_in_check(table, playing_team) is False:
                legal_moves.append(move)

        return legal_moves

    def finish_game(self, winner):
        self.game.game_ended = True
