########################
# Auteurs:
# Pierre Coucheney
# Toto Lehéro
# ...
# Groupe de TD:
# MPCI 5
########################

########################
# import des librairies

import tkinter as tk
import copy


########################
# Constantes

COULEUR_FOND = "grey100"
COULEUR_QUADR = "grey50"
COULEUR_VIVANT = "yellow"
LARGEUR = 600
HAUTEUR = 400
# la longueur des carrés qui constituent le quadrillage
COTE = 20
NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

######################
# Variables globales

tableau = None

########################
# fonctions


def quadrillage():
    """Affiche un quadrillage sur le canvas."""
    x0, x1 = 0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADR)
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADR)
        x += COTE


def coord_to_lg(x, y):
    """Fonction qui retourne la colonne et la ligne du quadrillage
    à partir des coordonnées x et y"""
    return x // COTE, y // COTE


def change_carre(event):
    """Change l'état du carré sur lequel on a cliqué"""
    i, j = coord_to_lg(event.x, event.y)
    if tableau[i][j] == -1:
        x, y = i * COTE, j * COTE
        carre = canvas.create_rectangle(x, y, x + COTE,
                                        y + COTE, fill=COULEUR_VIVANT,
                                        outline=COULEUR_QUADR)
        tableau[i][j] = carre
    else:
        canvas.delete(tableau[i][j])
        tableau[i][j] = -1


def creer_tableau():
    """initialise un tableau à deux dimensions qui vaut -1 partout
    -1 est pour une case morte
    identifiant du carré dessiné si une case est vivante
    tableau[i][j] est la valeur de la case à la colonne i et la ligne j
    """
    global tableau
    tableau = []
    for i in range(NB_COL):
        tableau.append([-1] * NB_LINE)
    # tableau = [tableau_col for i in range(NB_COL)]


def compte_vivant(i, j):
    """Retourne le nombre de cases voisines vivantes
       autour de la case (i, j)"""
    cpt = 0
    for k in range(max(0, i-1), min(NB_COL, i+2)):
        for el in range(max(0, j-1), min(NB_LINE, j+2)):
            if tableau[k][el] != -1 and [k, el] != [i, j]:
                cpt += 1
    return cpt


def traite_case(i, j):
    """Traite la case à la colonne i et ligne j en
       retournant la nouvelle valeur du tableau"""
    nb_vivant = compte_vivant(i, j)
    if tableau[i][j] == -1:
        if nb_vivant == 3:
            x, y = i * COTE, j * COTE
            carre = canvas.create_rectangle(x, y, x + COTE,
                                            y + COTE, fill=COULEUR_VIVANT,
                                            outline=COULEUR_QUADR)
            return carre
        else:
            return -1
    else:
        if nb_vivant != 2 and nb_vivant != 3:
            canvas.delete(tableau[i][j])
            return -1
        else:
            return tableau[i][j]


def etape(event):
    """Fait une étape du jeu de la vie"""
    global tableau
    tableau_res = copy.deepcopy(tableau)
    for i in range(NB_COL):
        for j in range(NB_LINE):
            tableau_res[i][j] = traite_case(i, j)
    tableau = tableau_res


def sauvegarder():
    """Sauvegarde le tableau dans le fichier sauvegarde.txt"""
    fic = open("sauvegarde.txt", "w")
    for j in range(NB_LINE):
        for i in range(NB_COL):
            fic.write(str(tableau[i][j]) + "\n")
    fic.close()


def charger():
    """Charger le fichier sauvegarde.txt dans le tableau"""
    fic = open("sauvegarde.txt", "r")
    cpt = 0
    for ligne in fic:
        i , j = cpt%NB_COL, cpt//NB_COL
        if tableau[i][j] != -1:
            canvas.delete(tableau[i][j])
        n = int(ligne)
        if n == -1:
            tableau[i][j] = -1
        else:
            x, y = i * COTE, j * COTE
            carre = canvas.create_rectangle(x, y, x + COTE,
                                            y + COTE, fill=COULEUR_VIVANT,
                                            outline=COULEUR_QUADR)
            tableau[i][j] = carre 
        cpt += 1          
    fic.close()


########################
# programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")
# création des widgets
canvas = tk.Canvas(racine, bg=COULEUR_FOND, width=LARGEUR, height=HAUTEUR)
quadrillage()
creer_tableau()
bout_sauv = tk.Button(racine, text="sauvegarder", command=sauvegarder)
bout_charger = tk.Button(racine, text="charger", command=charger)
# placement des widgets
canvas.grid(row=0, rowspan=2)
bout_sauv.grid(column=1, row=0)
bout_charger.grid(column=1, row=1)
# liaison des événements
canvas.bind("<Button-1>", change_carre)
racine.bind("n", etape)
# boucle principale
racine.mainloop()
