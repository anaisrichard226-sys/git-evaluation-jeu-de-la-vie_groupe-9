# Jeu de la vie

Simulation du jeu de la vie de Conway en Python (groupe 9).

## Installation

- Python 3
- `ffmpeg` (pour assembler la vidéo) : `sudo apt install python3 git ffmpeg gource`
- Sous Windows, utiliser WSL ou Git Bash.

Aucune bibliothèque Python externe n'est nécessaire.

## Exécution

Grille aléatoire, 21 images dans `outputs` :

    python3 main.py

Grille lue sur l'entrée standard, sortie texte :

    cat tests/matrix3/input.txt | python3 main.py -m 1 -t text

Résultat attendu :

    iteration: 1
    0 1 0
    0 0 1
    0 1 0

Même grille avec conditions périodiques :

    cat tests/matrix3/input.txt | python3 main.py -m 1 -p -t text

## Arguments

| Option courte | Option longue | Description | Défaut |
|---|---|---|---|
| `-n N` | `--nb_cells N` | nombre de cellules par côté | 10 |
| `-m N` | `--max_iterations N` | numéro de la dernière itération | 20 |
| `-s N` | `--seed N` | graine du générateur aléatoire | 42 |
| `-o DOSSIER` | `--output_directory DOSSIER` | dossier des images | `outputs` |
| `-t TYPE` | `--output_type TYPE` | `image` ou `text` | `image` |
| `-p` | `--periodic` | conditions aux limites périodiques | désactivé |
| `-h` | `--help` | affiche l'aide | |

## Vidéos

- Simulation (graine ..., commandes ...) : <lien YouTube>
- Gource : <lien YouTube>

## Intégration continue

Exécution réussie : <lien de l'onglet Actions>

## Auteurs

| Nom | Prénom | Numéro étudiant |
|---|---|---|
| ANDRIAMANANJARA | Ranto Ruannah Mialitiana | 45003854 |
| RAKOTOMAHARIVO | Miangaly Fitia | 45005628 |
| MBAE CHARIF | Mounira | 45005261 |
| SHUM-HUNG RAKOTOMANDIMBY | Ludovic | 46007322 |

## Liens utiles

- [Documentation argparse](https://docs.python.org/3/library/argparse.html)
- [Documentation random](https://docs.python.org/3/library/random.html)
- [Documentation ffmpeg](https://ffmpeg.org/documentation.html)
- [Gource](https://gource.io/)