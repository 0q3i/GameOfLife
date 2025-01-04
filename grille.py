from math import *
import cellule as c

class Grille:

    def __init__(self, x, y, l, h):
        self.longuer = l
        self.hauteur = h
        self.matrice = [[c.Cellule(False, False, x_c, x_y, self) for x_c in range(x)] for x_y in range(y)]
        self.lst_c = []  # Liste des cellules vivantes

    def tour(self):
        """Met à jour l'état des cellules"""
        for c_y in self.matrice:  # Parcours de toute la matrice
            for c_x in c_y:
                c_x.calcule_etat_futur()  # Calcule l'état futur de chaque cellule
                c_x.update()  # Met à jour l'état actuel de chaque cellule

    def voisin(self, cellule):
        """Renvoie la liste des voisins d'une cellule"""
        lst_voisin = []
        for y_offset in range(-1, 2):
            for x_offset in range(-1, 2):
                if y_offset == 0 and x_offset == 0:
                    continue  # On ignore la cellule elle-même
                x_voisin = cellule.x + x_offset
                y_voisin = cellule.y + y_offset
                if 0 <= x_voisin < len(self.matrice[0]) and 0 <= y_voisin < len(self.matrice):
                    lst_voisin.append(self.matrice[y_voisin][x_voisin])
        return lst_voisin

    def _ajoute(self, cellule):
        """Ajoute une cellule vivante à la liste"""
        self.lst_c.append(cellule)

    def _remove(self):
        """Enlève les cellules mortes"""
        self.lst_c = [cellule for lst_cellule in self.lst_c for cellule in lst_cellule if cellule.vivante]

# Test
g = Grille(10, 10, 1, 1)

# Création des cellules et ajout à la grille
A = c.Cellule(True, None, 10, 10, g)  # Passer l'instance de Grille à la cellule
B = c.Cellule(True, None, 10, 11, g)
C = c.Cellule(True, None, 20, 20, g)

g._ajoute(A)
g._ajoute(B)
g._ajoute(C)

# Exemple d'appel à la méthode voisin pour obtenir les voisins de la cellule à (11, 10)
lst_c_v = g.voisin(c.Cellule(True, None, 11, 10, g))
for elm in lst_c_v:
    print(elm)  # Affiche les voisins



