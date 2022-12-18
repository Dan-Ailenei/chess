from unittest.mock import Mock

import pytest

from chess.controller import ChessController, Game, Team
from chess.models import Pawn, Rook, King, Table


@pytest.fixture
def controller(table):
    return ChessController(Game(table))


@pytest.fixture
def table():
    return Table({(1, 0): Pawn(Team.WHITE)})


def test_is_move_legal_returns_false_when_initial_position_does_not_have_piece(controller):
    is_legal = controller.is_move_legal((5, 5), (6, 6))
    assert is_legal is False


def test_is_move_legal_returns_true_when_to_position_is_in_legal_moves(table, controller):
    controller._get_all_legal_moves_for_piece = lambda x, y: [(6, 6)]

    is_legal = controller.is_move_legal((1, 0), (6, 6))

    assert is_legal is True


def test_table_move_piece_works(table):
    table = table.move_piece((1, 0), (2, 0))

    assert table.get_piece((2, 0)) == Pawn(Team.WHITE)


def test_get_all_legal_moves_for_piece_filters_check_discoveries(controller, table):
    pawn = table.get_piece((1, 0))
    pawn.get_moves = lambda x, y : [(2, 0), (3, 0)]

    def is_in_check(table, playing_team):
        return table.get_piece((3, 0)) == Pawn(Team.WHITE)

    controller._is_in_check = is_in_check

    assert controller._get_all_legal_moves_for_piece(table, (1, 0)) == [(2, 0)]


def test_table_is_in_check_works():
    table = Table({(1, 0): Pawn(Team.WHITE), (2, 0): King(Team.BLACK)})
    controller = ChessController(Game(table))

    controller._get_all_legal_moves_for_piece = Mock(return_value=[(2, 0)])

    is_in_check = controller._is_in_check(table, Team.BLACK)

    controller._get_all_legal_moves_for_piece.assert_called_with(table, (1, 0), filter_moves_that_lead_to_check=False)
    assert is_in_check is True


def test_table_is_mate_returns_true_when_mate():
    table = Table(
        {(1, 0): Pawn(Team.WHITE), (2, 0): Pawn(Team.WHITE), (5, 5): King(Team.BLACK)}
    )
    controller = ChessController(Game(table))

    def get_all_pieces_moves_of_team(table, team, filter_moves_that_lead_to_check=True):
        if team == Team.WHITE:
            return {(2, 0): [(5, 5)], (1, 0): [(6, 6), (6, 4), (4, 6), (4, 4), (4, 5), (6, 5), (5, 4), (5, 6)]}
        else:
            return {}

    controller._get_all_pieces_moves_of_team = get_all_pieces_moves_of_team

    is_mate = controller._is_mate(table, Team.BLACK)

    assert is_mate is True


def test_table_is_in_check_return_mate_false_when_piece_can_be_eaten():
    # this is a mistake, tests should depend on some fake Pieces implementing the interface, not using actual pieces
    table = Table(
        {(7, 0): Rook(Team.WHITE), (6, 1): Rook(Team.WHITE), (7, 7): Rook(Team.BLACK), (0, 1): King(Team.BLACK)}
    )
    controller = ChessController(Game(table))

    def get_all_pieces_moves_of_team(table, team, filter_moves_that_lead_to_check=True):
        if team == Team.WHITE:
            return {(6, 1): [(0, 1), (1, 2), (1, 0), (1, 1), (0, 0), (0, 2)]}
        else:
            return {(7, 7): (7, 0)}

    controller._get_all_pieces_moves_of_team = get_all_pieces_moves_of_team

    is_mate = controller._is_mate(table, Team.BLACK)

    assert is_mate is False
