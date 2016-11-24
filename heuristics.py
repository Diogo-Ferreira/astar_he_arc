from math import sqrt


def h0(next, to):
    return 0


def h1(next, to):
    return abs(next.x_pos - to.x_pos)


def h2(next, to):
    return abs(next.y_pos - to.y_pos)


def h3(next, to):
    return sqrt(pow(abs(next.y_pos - to.y_pos), 2) + pow(abs(next.x_pos - to.x_pos), 2))


def h4(next, to):
    return abs(next.y_pos - to.y_pos) + abs(next.x_pos - to.x_pos)