import abc
import enum
from copy import deepcopy
from dataclasses import dataclass
from typing import Type, Optional

from chess.maxtrix import traverse_matrix, MatrixDirection, get_box_positions

Position = tuple[int, int]


class Team(enum.Enum):
    WHITE = 1
    BLACK = 2

    @classmethod
    def get_oponent(cls, team):
        return Team.WHITE if team == team.BLACK else team.BLACK


@dataclass
class Piece(abc.ABC):
    team: Team

    @abc.abstractmethod
    def get_moves(self, position, table: 'Table') -> list[Position]:
        pass


    def is_piece_from_different_team(self, table, position):
        return (op := table.get_piece(position)) is not None and op.team != self.team


class Table:
    def __init__(self, pieces):
        self._pieces: dict[Position, Type[Piece]] = pieces
        self.last_move: Optional[Position, Position] = None

    def get_piece(self, position) -> Type[Piece]:
        return self._pieces.get(position)

    def get_king_position(self, team):
        for position, piece in self._pieces.items():
            if piece == King(team):
                return position

        raise ValueError('King not on table')

    @classmethod
    def build_initial_table(cls):
        return cls(
            {
                (0, 3): King(Team.WHITE),
                (7, 3): King(Team.BLACK),

                (0, 0): Rook(Team.WHITE),
                (0, 7): Rook(Team.WHITE),

                (7, 0): Rook(Team.BLACK),
                (7, 7): Rook(Team.BLACK)
            }
        )

    def move_piece(self, piece_position, to_position):
        new_table = deepcopy(self)

        piece = new_table._pieces.pop(piece_position)
        if isinstance(piece, Pawn) and to_position[0] == 0 or to_position[0] == 7:
            piece = piece.promote()

        new_table._pieces[to_position] = piece
        new_table.last_move = (piece_position, to_position)

        return new_table

    def get_piece_positions(self, team: Team, filter_king=True):
        for position, piece in self._pieces.items():
            if piece.team == team and isinstance(piece, King) is False:
                yield position


@dataclass
class Game:
    table: Table
    team_to_play: Team = Team.WHITE
    game_ended: bool = False


class Bishop(Piece):
    def get_moves(self, position, table) -> list[Position]:
        top_right = traverse_table_direction_stream(table, position, MatrixDirection.TOP_RIGHT)
        top_left = traverse_table_direction_stream(table, position, MatrixDirection.TOP_LEFT)
        bottom_right = traverse_table_direction_stream(table, position, MatrixDirection.BOTTOM_RIGHT)
        bottom_left = traverse_table_direction_stream(table, position, MatrixDirection.BOTTOM_LEFT)

        return top_right + top_left + bottom_right + bottom_left


class Rook(Piece):
    def get_moves(self, position, table) -> list[Position]:
        bottom = traverse_table_direction_stream(table, position, MatrixDirection.BOTTOM)
        up = traverse_table_direction_stream(table, position, MatrixDirection.UP)
        left = traverse_table_direction_stream(table, position, MatrixDirection.LEFT)
        right = traverse_table_direction_stream(table, position, MatrixDirection.RIGHT)

        return bottom + up + left + right


class Queen(Piece):
    def get_moves(self, position, table) -> list[Position]:
        return Bishop(self.team).get_moves(position, table) + Rook(self.team).get_moves(position, table)


class Knight(Piece):
    def get_moves(self, position, table) -> list[Position]:
        x, y = position

        possible_moves = [
            (x + 2, y - 1), (x + 2, y + 1),
            (x - 2, y - 1), (x - 2, y + 1),
            (x + 1, y - 2), (x - 1, y - 2),
            (x + 1, y + 2), (x - 1, y + 2),
        ]
        legal_moves = []
        for move in possible_moves:
            if 0 <= x < 8 and 0 <= y < 8 and (table.get_piece(move) is None or self.is_piece_from_different_team(table, position)):
                legal_moves.append(move)

        return [(x, y) for x, y in possible_moves]


class Pawn(Piece):
    def get_moves(self, position, table: 'Table') -> list[Position]:
        x, y = position
        direction_vector = 1 if table.get_piece(position).team == Team.WHITE else -1

        up_direction = MatrixDirection.UP if direction_vector == 1 else MatrixDirection.BOTTOM
        top_right_direction = MatrixDirection.TOP_RIGHT if direction_vector == 1 else MatrixDirection.BOTTOM_LEFT
        top_left_direction = MatrixDirection.TOP_LEFT if direction_vector == 1 else MatrixDirection.BOTTOM_RIGHT

        up = next(traverse_matrix(position, up_direction))
        top_right = next(traverse_matrix(position, top_right_direction))
        top_left = next(traverse_matrix(position, top_left_direction))

        legal_moves = []
        if table.get_piece(up) is None:
            legal_moves.append(up)

        en_passant_top_right_move = ((x - (2 * direction_vector), y + direction_vector), (x, y + direction_vector))
        en_passant_top_left_move = ((x - (2 * direction_vector), y - direction_vector), (x, y - direction_vector))

        if self.is_piece_from_different_team(table, top_right) or (table.last_move == en_passant_top_right_move and isinstance(table.get_piece(table.last_move[1]), Pawn)):
            legal_moves.append(top_right)
        if self.is_piece_from_different_team(table, top_left) or (table.last_move == en_passant_top_left_move and isinstance(table.get_piece(table.last_move[1]), Pawn)):
            legal_moves.append(top_left)

        return legal_moves

    def promote(self):
        return Queen(self.team)


class King(Piece):

    def get_moves(self, position, table: 'Table') -> list[Position]:
        box_positions = get_box_positions(position)

        legal_moves = []
        for pos in box_positions:
            oponent_king_in_box_of_box = any(isinstance(table.get_piece(p), King) and self.is_piece_from_different_team(table, p) for p in get_box_positions(pos))
            if oponent_king_in_box_of_box is False:
                legal_moves.append(pos)

        return legal_moves


def traverse_table_direction_stream(table, position, direction):
    valid_positions = []

    current_piece = table.get_piece(position)
    oponent_team = Team.get_oponent(current_piece.team)

    for pos in traverse_matrix(position, direction):
        table_piece = table.get_piece(pos)
        if table_piece is None:
            valid_positions.append(pos)
        else:
            if table_piece.team == oponent_team:
                valid_positions.append(pos)
            break

    return valid_positions
