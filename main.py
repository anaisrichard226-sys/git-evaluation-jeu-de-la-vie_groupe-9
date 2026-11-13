import random

from lib import write_grid


def compter_voisins_vivants(grille, ligne, colonne):
    n = len(grille)
    compteur = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                voisins_ligne = ligne + i
                voisins_colonne = colonne + j
                if 0 <= voisins_ligne < n and 0 <= voisins_colonne < n:
                    if grille[voisins_ligne][voisins_colonne] == 1:
                        compteur += 1
    return compteur


def generation_suivante(grille):
    n = len(grille)
    nouvelle_grille = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            nb_voisins = compter_voisins_vivants(grille, i, j)
            if grille[i][j] == 1:
                if nb_voisins == 2 or nb_voisins == 3:
                    nouvelle_grille[i][j] = 1
            else:
                if nb_voisins == 3:
                    nouvelle_grille[i][j] = 1
    return nouvelle_grille


def main():
    nb_cells = 50

    rng = random.Random(4200)

    matrix = [
        [rng.choice([0, 1]) for _ in range(nb_cells)]
        for _ in range(nb_cells)
    ]

    iter = 0
    filename = f"outputs/grid_{iter:04d}.png"
    write_grid(matrix=matrix, filename=filename)

if __name__ == "__main__":
    main()


