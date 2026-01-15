DEPLACEMENT_FOU = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
    (2, 2),
    (2, -2),
    (-2, 2),
    (-2, -2),
    (3, 3),
    (3, -3),
    (-3, 3),
    (-3, -3),
    (4, 4),
    (4, -4),
    (-4, 4),
    (-4, -4),
    (5, 5),
    (5, -5),
    (-5, 5),
    (-5, -5),
    (6, 6),
    (6, -6),
    (-6, 6),
    (-6, -6),
    (7, 7),
    (7, -7),
    (-7, 7),
    (-7, -7),
]
DEPLACEMENT_TOUR = []
for i in range(1, 8):
    DEPLACEMENT_TOUR.append((0, i))
    DEPLACEMENT_TOUR.append((0, -i))
    DEPLACEMENT_TOUR.append((i, 0))
    DEPLACEMENT_TOUR.append((-i, 0))

DEPLACEMENT_REINE = DEPLACEMENT_FOU + DEPLACEMENT_TOUR

DEPLACEMENT_CAVALIER = [
    (1, 2),
    (2, 1),
    (-1, 2),
    (-2, 1),
    (1, -2),
    (2, -1),
    (-1, -2),
    (-2, -1),
]

DEPLACEMENT_ROI = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
]

############ POUR LE SERVEUR ############

PORT = 5503
IP = "localhost" #modifier pour modifier l'adresse IP de l'hôte auquel le client accède
