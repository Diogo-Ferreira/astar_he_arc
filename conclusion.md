# TP A* cours Intélligence artificielle
Le programme a été développé en python 3.5 dans un venv, pour le lancer veuillez tout d'abord vérifier que les fichiers connections.txt et  positions.txt sont dans le même répértoire que astar.py.

Pour lancer le programme: ```python3 astar.py Warsaw Lisbon```


## heuristiques
Toutes les heuristiques sont admissibles parce qu'elles valent 0 à la distination.

Elles sont toutes consistantes, sauf manathan qui peut sur-estimer le coût.

## Question 1
Oui, car cela va influencer l'ordre des villes dans la frontière, donc la probabilité que la ville retirée soit différente sera plus grande. Comme on peux le voir dans l'exemple.

```
$ python3 astar.py Warsaw Lisbon

with h0
['Warsaw', 'Berlin', 'Hamburg', 'Amsterdam', 'Brussels', 'Paris', 'Madrid', 'Lisbon']
Gone through 2398.0 km, with 19 visited cities
with h1
...
Gone through 2398.0 km, with 18 visited cities
with h2
...
Gone through 2398.0 km, with 19 visited cities
with h3
...
Gone through 2398.0 km, with 18 visited cities
with h4
...
Gone through 2398.0 km, with 16 visited cities

```

## Question 2
Avec le calculs de g(x) courant (km parcourus), je n'ai pas réussit à trouvé un chemin alternatif. Un chemin alternatif peut être trouvé un mettant le gx = 0, car ainsi seul les h(x) feront le cout, et donc on aura une différence d'itinéraire entre un vol d'oiseau et une différence en X.

## Question 3
Pour un voyage en voiture, où on roulera beaucoup en autoroute, on préférera le vol d'oiseau, car la plupart des autoroutes sont droites.
Dans une ville telle que new york ou dans une grille, ça sera la distance manathan, car on ses deplace en (haut,bas,gauche,droite).

Pour les différences en x ou y, on peut imaginer que cela peut être utile dans un graphique à une dimension.

_Ferreira Venancio Diogo, INF3-DLMA_
