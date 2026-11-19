import random
import sys

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

def erreur(message):
    """Écrit un message sur STDERR et quitte avec un code d'erreur."""
    print(f"Erreur : {message}", file=sys.stderr)
    sys.exit(1)


def lire_grille_stdin():
    """Lit une grille sur l'entrée standard.

    Format : une première ligne avec la taille n, puis n lignes
    de n cellules (0 ou 1) séparées par des espaces.
    """
    lignes = [l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
    if not lignes:
        erreur("grille vide")
    try:
        n = int(lignes[0])
    except ValueError:
        erreur("la première ligne doit contenir la taille de la grille (un entier)")
    if n <= 0:
        erreur("la taille de la grille doit être strictement positive")
    if len(lignes) - 1 != n:
        erreur(f"{n} lignes attendues, {len(lignes) - 1} reçues")

    grille = []
    for numero, ligne in enumerate(lignes[1:], start=2):
        cellules = ligne.split()
        if len(cellules) != n:
            erreur(f"ligne {numero} : {n} cellules attendues, {len(cellules)} reçues")
        for cellule in cellules:
            if cellule not in ("0", "1"):
                erreur(f"ligne {numero} : cellule invalide '{cellule}' (0 ou 1 attendu)")
        grille.append([int(c) for c in cellules])
    return grille


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
