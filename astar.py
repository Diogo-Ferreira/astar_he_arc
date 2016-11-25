"""
Ferreira Venancio Diogo
IA Class HE-ARC 2016

Main module

Note : I choose to not write a state class like the last exercise,
 because I don't feel the need for it to this simple problem,
 but it's true that it would be more generic with a state class.
"""
import sys
from files_parsing import load_connections, load_cities, trace_to
from heuristics import *


def search(fromCityName, toCityName, cities, heuristicFunction):
    """
    Search the min path between 2 cities, using the heuristicFunction as h(x) for the cost
    :param fromCityName: name of the start city
    :param toCityName: name of the target city
    :param cities: dict of cities objects
    :param heuristicFunction: h(x)
    :return: target city object, who's parent contains the path (go through every parent)
    """
    frontier = [cities[fromCityName]]
    # stores the last cost of the city in frontier, much efficient than to look in the front
    costs_to = {}
    history = set()
    history.add(frontier[0])
    target_city = cities[toCityName]

    log = "** with %s going to %s from %s **\n" % (heuristicFunction.__name__, toCityName, fromCityName)

    while frontier:

        log += "front=[%s] \n" % ", ".join(["'%s'" % str(f) for f in frontier])

        log += "his=[%s] \n" % ", ".join(["'%s'" % str(h) for h in history])

        current_city = frontier.pop()

        gx = current_city.gx

        history.add(current_city)

        if current_city == target_city:
            return current_city, history, log

        for neighbour_name, dist in current_city:

            # If the neighbour is already in front, but the path from the current is cheaper
            if neighbour_name in costs_to and gx + dist < costs_to[neighbour_name]:
                frontier.remove(neighbour_name)

            if neighbour_name not in history and neighbour_name not in frontier:
                costs_to[neighbour_name] = gx + dist

                next_city_inst = cities[neighbour_name]

                next_city_inst.gx, next_city_inst.parent = costs_to[neighbour_name], current_city

                frontier.append(next_city_inst)

        frontier.sort(reverse=True, key=lambda c: (c.gx + heuristicFunction(c, target_city)))


def astart(h, cities, fromCity='Warsaw', toCity='Lisbon'):
    """
    Initiates the aster algorithm, and goes through every city of the path
    :param h: h(X)
    :param cities: dict of cities objects
    :param fromCity: start city name
    :param toCity: target city name
    """
    print("with %s" % h.__name__)

    city, hist, log = search(fromCity, toCity, cities, h)

    parent, dist = city, city.gx

    path = []

    # Creates the path, by going throug each parent
    while parent:
        path.append(parent.name)
        parent = parent.parent

    resultOut = "Gone through %s km, with %s visited cities" % (dist, len(hist))

    log += "Path : %s \n" % str(path[::-1]) + resultOut

    # Writes to astar.log
    trace_to(log)

    print(path[::-1])

    print(resultOut)


if __name__ == "__main__":
    """
    How to: python3 astar.py Warsaw Lisbon
    this will run every h(s), and dump everything in astar.log
    """
    city_file = "positions.txt"

    connections_file = "connections.txt"

    cities = load_cities(city_file)

    cities = load_connections(cities, connections_file)

    fromCity, toCity = sys.argv[1], sys.argv[2]

    astart(h0, cities, fromCity, toCity)
    astart(h1, cities, fromCity, toCity)
    astart(h2, cities, fromCity, toCity)
    astart(h3, cities, fromCity, toCity)
    astart(h4, cities, fromCity, toCity)
