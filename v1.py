import grille as g
import cellule as c
from time import sleep

# fichier test

<<<<<<< HEAD
reg = g.Grille(40, 40)  # Création d'une grille de 10x10 avec des cellules de taille 1x1
=======
reg = g.Grille(50, 40)  # Création d'une grille de 10x10 avec des cellules de taille 1x1
>>>>>>> db3cb9fd1b89cd8180ab660297aa05f400e2b518

# Création des cellules et ajout à la grille
config = input("donne une lettre de l'aphbet romain en majuscule:")

if config == "A":
    A = c.Cellule(True, None, 1, 1)
    B = c.Cellule(True, None, 2, 2)
    C = c.Cellule(True, None, 2, 3)
    D = c.Cellule(True, None, 1, 3)
    E = c.Cellule(True, None, 0, 3)
    reg.mat_ajoute(A)
    reg.mat_ajoute(B)
    reg.mat_ajoute(C)
    reg.mat_ajoute(D)
    reg.mat_ajoute(E)
elif config == "B":
    A = c.Cellule(True, None, 1, 1)
    B = c.Cellule(True, None, 1, 2)
    C = c.Cellule(True, None, 1, 3)
    reg.mat_ajoute(A)
    reg.mat_ajoute(B)
    reg.mat_ajoute(C)
elif config == "C":
    A = c.Cellule(True, None, 1, 1)
    B = c.Cellule(True, None, 2, 1)
    C = c.Cellule(True, None, 1, 2)
    D = c.Cellule(True, None, 2, 2)
    reg.mat_ajoute(A)
    reg.mat_ajoute(B)
    reg.mat_ajoute(C)
    reg.mat_ajoute(D)
elif config == "D":
    lst_pos= [(1,15),(2,15),(1,16),(2,16),(11,15),(11,16),(11,14),(12,13),
              (13,12),(14,12),(12,17),(13,18),(14,18),(15,15),(16,13),(17,14),
              (17,15),(18,15),(17,16),(16,17),(21,16),(22,16),(21,17),(22,17),
              (21,18),(22,18),(23,15),(25,15),(25,14),(23,19),(25,19),(25,20),
              (39,18),(40,18),(39,17),(40,17)
              ]
    for elm in lst_pos:
        A = c.Cellule(True,None,elm[0],elm[1])
        reg.mat_ajoute(A)




reg.mat() #methode STR
print("debut")
while True:
    #modifie la grill enfonction de la cellule
    reg.tour()
    print("fin")
    #print dans la console la grille
    reg.mat()
    #fps
    sleep(2)