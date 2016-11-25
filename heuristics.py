"""
Ferreira Venancio Diogo
IA Class HE-ARC 2016
This modules holds the heuristics functions
"""
from math import sqrt


def h0(current, to):
    return 0


def h1(current, to):
    """
    Computes the absolute x diff of 2 cities
    :param current: current city
    :param to: target citiy
    :return: posivite float (x diff)
    """
    return abs(current.x_pos - to.x_pos)


def h2(current, to):
    """
    Computes the absolute y diff of 2 cities
    :param current: current city
    :param to: target citiy
    :return: posivite float (y diff)
    """
    return abs(current.y_pos - to.y_pos)


def h3(current, to):
    """
    Computes the direct (bird fly) distance of 2 cities
    :param current: current city
    :param to: target city
    :return: posivite float (distance)
    """
    return sqrt(pow(abs(current.y_pos - to.y_pos), 2) + pow(abs(current.x_pos - to.x_pos), 2))


def h4(current, to):
    """
    Computes the manhattan distance of 2 cities
    :param current: current city
    :param to: target city
    :return: posivite float (man distance)
    """
    return abs(current.y_pos - to.y_pos) + abs(current.x_pos - to.x_pos)