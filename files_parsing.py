from City import City


def load_cities(city_file_name):
    with open(city_file_name) as city_file_handler:
        return {l.split()[0]: City(*l.split()) for l in city_file_handler}


def load_connections(cities, connections_file_name):
    with open(connections_file_name) as connections_file_handler:
        for line in connections_file_handler:
            fromCity, toCity, distance = line.split()

            cities[fromCity].add_connection_to(toCity, distance)

            cities[toCity].add_connection_to(fromCity, distance)

    return cities


def trace_to(content, filename='astar.log'):
    with open(filename, mode='a') as f:
        f.write("%s \nEND \n\n" % content)