"""
Ferreira Venancio Diogo
IA Class HE-ARC 2016
This module holds the parsing files methods
"""
from City import City


def load_cities(city_file_name):
    """
    Creates a city object <cityName,cityObject> from a specified file
    :param city_file_name: the name of the file which holds the data
    :return: dict<cityName,cityObject>
    """
    with open(city_file_name) as city_file_handler:
        return {l.split()[0]: City(*l.split()) for l in city_file_handler}


def load_connections(cities, connections_file_name):
    """
    Creates the cities connections between them from a file.
    :param cities: dict of cities
    :param connections_file_name: file which holds the connections data
    :return: dict of cities, with the cities updated with their respective connections
    """
    with open(connections_file_name) as connections_file_handler:
        for line in connections_file_handler:
            fromCity, toCity, distance = line.split()

            cities[fromCity].add_connection_to(toCity, distance)

            cities[toCity].add_connection_to(fromCity, distance)

    return cities


def trace_to(content, filename='astar.log'):
    """
    Write the content on a log file
    :param content: content
    :param filename: file to writo to
    """
    with open(filename, mode='a') as f:
        f.write("%s \nEND \n\n" % content)