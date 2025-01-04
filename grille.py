from math import *
import cellule as c

class Grille:

    def __init__(self, x, y, l, h):
        self.longuer = l
        self.hauteur = h
        self.matrice = [[c.Cellule(False, False, x_c, x_y, self) for x_c in range(x)] for x_y in range(y)]
        self.lst_c = []

    def tour(self):
        """Met à jour l'état des cellules"""
        for c in self.lst_c:
            c.calcule_etat_futur()
            c.update()

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
        self.lst_c = [cellule for cellule in self.lst_c if cellule.vivante]

# Test
A = c.Cellule(True, None, 10, 10, None)
B = c.Cellule(True, None, 10, 11, None)
C = c.Cellule(True, None, 20, 20, None)

g = Grille(10, 10, 1, 1)
g._ajoute(A)
g._ajoute(B)
g._ajoute(C)

lst_c_v = g.voisin(c.Cellule(True, None, 11, 10, None))
for elm in lst_c_v:
    print(elm)





