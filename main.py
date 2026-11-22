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
                if periodique:
                    voisins_ligne = voisins_ligne % n
                    voisins_colonne = voisins_colonne % n
                if (voisins_ligne >= 0 and voisins_ligne < n) and (voisins_colonne >= 0 and voisins_colonne < n):
                    if grille[voisins_ligne][voisins_colonne] == 1:
                        compteur += 1
    
    return compteur



def generation_suivante(grille, periodique=False):
    n = len(grille)
    nouvelle_grille = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            nb_voisins = compter_voisins_vivants(grille, i, j, periodique)
            if grille[i][j] == 1:
                if nb_voisins == 2 or nb_voisins == 3:
                    nouvelle_grille[i][j] = 1
            else:
                if nb_voisins == 3:
                    nouvelle_grille[i][j] = 1
    return nouvelle_grille


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
    print(f"iteration: {numero}")
    for ligne in grille:
        print(' '.join([str(cell) for cell in ligne]))


def main():
    args = lire_arguments()

    if not sys.stdin.isatty():
        grille = lire_grille_stdin()
    else:
        grille = creer_grille_aleatoire(args.nb_cells, args.seed)

    images = args.output_type == "image"
    if images:
        ecrire_images(grille, 0, args.output_directory)

    for numero in range(1, args.max_iterations + 1):
        grille = generation_suivante(grille, args.periodic)
        if images:
            ecrire_images(grille, numero, args.output_directory)

    if images:
        print(f"Generation of {args.max_iterations + 1} images in directory {args.output_directory}")
    else:
        afficher_texte(grille, args.max_iterations)


if __name__ == "__main__":
    main()
