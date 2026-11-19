import random
import os
import sys
import argparse


from lib import write_grid
#----------- Tâche A : calcul des générations ----------------

def compter_voisins_vivants(grille, ligne, colonne, periodique=False):
    n = len(grille)
    compteur = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                voisins_ligne = ligne + i
                voisins_colonne = colonne + j
                if (voisins_ligne >= 0 and voisins_ligne < n) and (voisins_colonne >= 0 and voisins_colonne < n):
                    if grille[voisins_ligne][voisins_colonne] == 1:
                        compteur += 1
    
    return compteur



def generation_suivante(grille, periodique=False):
    pass


#----------- Tâche B : arguments de la ligne de commande ------


def lire_arguments():
    parser = argparse.ArgumentParser(description="Jeu de la vie de Conway")
    parser.add_argument("-n", "--nb_cells", type=int, default=10, help="nombre de cellules par côté (défaut : 10)")
    parser.add_argument("-m", "--max_iterations", type=int, default=20, help="numéro de la dernière itération (défaut : 20)")
    parser.add_argument("-s", "--seed", type=int, default=42, help="graine du générateur aléatoire (défaut : 42)")
    parser.add_argument("-o", "--output_directory", default="outputs", help="dossier des images (défaut : outputs)")
    parser.add_argument("-t", "--output_type", choices=["image", "text"], default="image", help="type de sortie : image ou text (défaut : image)")
    parser.add_argument("-p", "--periodic", action="store_true", help="active les conditions aux limites périodiques")
    args = parser.parse_args()

    if args.nb_cells <= 0:
        parser.error("--nb_cells doit être un entier strictement positif")
    if args.max_iterations < 0:
        parser.error("--max_iterations doit être un entier positif ou nul")

    return args



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
    os.makedirs(dossier, exist_ok=True)
    filename = os.path.join(dossier, f"grid_{numero:04d}.png")
    write_grid(matrix=grille, filename=filename)


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
