import grille as g
import cellule as c
from time import sleep

# fichier test

reg = g.Grille(10, 10, 1, 1)  # Création d'une grille de 10x10 avec des cellules de taille 1x1

# Création des cellules et ajout à la grille
config = input("donne une lettre de l'aphbet romain en majuscule:")

if config == "A":
    A = c.Cellule(True, None, 1, 1, g)
    B = c.Cellule(True, None, 2, 2, g)
    C = c.Cellule(True, None, 2, 3, g)
    D = c.Cellule(True, None, 1, 3, g)
    E = c.Cellule(True, None, 0, 3, g)
    reg.mat_ajoute(A)
    reg.mat_ajoute(B)
    reg.mat_ajoute(C)
    reg.mat_ajoute(D)
    reg.mat_ajoute(E)
elif config == "B":
    A = c.Cellule(True, None, 1, 1, g)
    B = c.Cellule(True, None, 1, 2, g)
    C = c.Cellule(True, None, 1, 3, g)
    reg.mat_ajoute(A)
    reg.mat_ajoute(B)
    reg.mat_ajoute(C)
elif config == "C":
    A = c.Cellule(True, None, 1, 1, g)
    B = c.Cellule(True, None, 2, 1, g)
    C = c.Cellule(True, None, 1, 2, g)
    D = c.Cellule(True, None, 2, 2, g)
    reg.mat_ajoute(A)
    reg.mat_ajoute(B)
    reg.mat_ajoute(C)
    reg.mat_ajoute(D)


reg.mat()
print("debut")
while True:
    #calcule
    reg.tour()
    print("fin")
    #console
    reg.mat()
    #fps
    sleep(1)