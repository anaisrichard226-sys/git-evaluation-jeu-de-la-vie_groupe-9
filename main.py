import random

from lib import write_grid

#----------- Tâche A : calcul des générations ----------------

def compter_voisins_vivants(grille, ligne, colonne, periodique=False):
    pass



def generation_suivante(grille, periodique=False):
    pass


#----------- Tâche B : arguments de la ligne de commande ------


def lire_arguments():
    pass

#------------ Tâche C : entrées et sorties ---------------------

def creer_grille_aleatoire(nb_cells, seed):
    """Crée une grille carrée aléatoire, reproductible grâce à la graine."""
    rng = random.Random(seed)
    return [
        [rng.choice([0, 1]) for _ in range(nb_cells)]
        for _ in range(nb_cells)
    ]

def lire_grille_stdin():
    pass


def ecrire_images(grille, numero, dossier):
    pass


def afficher_texte(grille, numero):
    pass




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
