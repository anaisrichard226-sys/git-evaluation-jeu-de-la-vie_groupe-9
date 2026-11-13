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


