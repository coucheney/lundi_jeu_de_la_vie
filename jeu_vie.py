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


########################
# Constantes

COULEUR_FOND = "grey100"
LARGEUR = 600
HAUTEUR = 400


########################
# fonctions

def quadrillage():
    """Affiche un quadrillage sur le canvas."""
    pass


########################
# programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")
# création des widgets
canvas = tk.Canvas(racine, bg=COULEUR_FOND, width=LARGEUR, height=HAUTEUR)
quadrillage()
# placement des widgets
canvas.grid(row=0)
# boucle principale
racine.mainloop()
