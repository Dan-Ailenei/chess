import enum


class MatrixDirection(enum.Enum):
    TOP_RIGHT = (1, 1)
    TOP_LEFT = (1, -1)
    BOTTOM_RIGHT = (-1, 1)
    BOTTOM_LEFT = (-1, -1)

    BOTTOM = (-1, 0)
    UP = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def traverse_matrix(position, direction:  MatrixDirection):
    x, y = position
    x_inc, y_inc = direction.value

    while True:
        x = x + x_inc
        y = y + y_inc

        yield x, y


def get_box_positions(position):
    box_positions = []
    for d in MatrixDirection:
        box_position = next(traverse_matrix(position, d))

        box_positions.append(box_position)

    return box_positions
