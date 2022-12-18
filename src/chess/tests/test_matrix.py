from chess.maxtrix import traverse_matrix, MatrixDirection, get_box_positions


def test_traverse_diagonal_top_right():
    generator = traverse_matrix((1, 1), MatrixDirection.TOP_RIGHT)
    coord1 = next(generator)
    coord2 = next(generator)

    assert coord1 == (2, 2)
    assert coord2 == (3, 3)


def test_traverse_diagonal_bottom():
    generator = traverse_matrix((5, 5), MatrixDirection.BOTTOM)
    coord1 = next(generator)
    coord2 = next(generator)

    assert coord1 == (4, 5)
    assert coord2 == (3, 5)


def test_get_coord_box_returns_all_positions():
    box = get_box_positions((5, 5))
    assert set(box) == {(4, 5), (6, 5), (5, 4), (5, 6), (6, 6), (4, 6), (4, 4), (6, 4)}


def test_get_coord_box_returns_filtered_positions():
    box = get_box_positions((7, 7))
    assert set(box) == {(6, 8), (6, 7), (7, 6), (6, 6), (7, 8)}
