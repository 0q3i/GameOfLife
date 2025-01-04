from math import *
import cellule as c

# Définition de la classe Grille qui représente la grille du jeu
class Grille:

    def __init__(self, x, y, l, h):
        """
        Initialisation de la grille.
        
        Paramètres :
        x : nombre de colonnes de la grille
        y : nombre de lignes de la grille
        l : longueur de chaque cellule
        h : hauteur de chaque cellule
        """
        self.longuer = l  # Stocke la longueur des cellules
        self.hauteur = h  # Stocke la hauteur des cellules

        # Création de la matrice représentant la grille. Chaque cellule est une instance de Cellule
        # La grille est de taille x par y et chaque cellule est initialisée avec des valeurs par défaut
        # La Coordonnee 0 0 ce trouve toujour en haut a gauche
        self.matrice = [[c.Cellule(False, False, x_c, x_y, self) for x_c in range(x)] for x_y in range(y)]

        self.lst_c = []  # Liste des cellules vivantes

    def tour(self):
        """
        Met à jour l'état de toutes les cellules de la grille.
        
        Cette méthode calcule l'état futur de chaque cellule et le met à jour.
        """
        for c_y in self.matrice:  # Parcours la matrice
            for c_x in c_y:
                c_x.calcule_etat_futur()  # Calcule l'état futur de la cellule
                c_x.update()  # Met à jour l'état actuel de la cellule avec l'état futur

    def voisin(self, cellule):
        """
        Renvoie la liste des voisins d'une cellule.
        
        Paramètre :
        cellule : la cellule dont on souhaite trouver les voisins
        
        Retourne :
        lst_voisin : liste des cellules voisines de la cellule donnée
        """
        lst_voisin = []  # Initialisation de la liste des voisins
        for y_offset in range(-1, 2):  # Parcours des voisins dans la direction verticale
            for x_offset in range(-1, 2):  # Parcours des voisins dans la direction horizontale
                if y_offset == 0 and x_offset == 0:
                    continue  # On ignore la cellule elle-même, pas de voisinage pour soi-même
                
                # Calcul des coordonnées du voisin
                x_voisin = cellule.x + x_offset
                y_voisin = cellule.y + y_offset

                # Vérification que le voisin est dans les limites de la grille
                if 0 <= x_voisin < len(self.matrice[0]) and 0 <= y_voisin < len(self.matrice):
                    lst_voisin.append(self.matrice[y_voisin][x_voisin])  # Ajout du voisin valide à la liste
        return lst_voisin  # Retourne la liste des voisins

    def _ajoute(self, cellule):
        """
        Ajoute une cellule vivante à la liste des cellules vivantes.
        
        Paramètre :
        cellule : la cellule vivante à ajouter à la liste
        """
        self.lst_c.append(cellule)  # Ajout de la cellule à la liste des cellules vivantes

    def _remove(self):
        """
        Enlève les cellules mortes de la liste des cellules vivantes.
        """
        # La liste est mise à jour pour ne garder que les cellules vivantes
        self.lst_c = [cellule for lst_cellule in self.lst_c for cellule in lst_cellule if cellule.vivante]

# Test
g = Grille(10, 10, 1, 1)  # Création d'une grille de 10x10 avec des cellules de taille 1x1

# Création des cellules et ajout à la grille
A = c.Cellule(True, None, 10, 10, g)
B = c.Cellule(True, None, 10, 11, g)
C = c.Cellule(True, None, 20, 20, g)
g._ajoute(A)
g._ajoute(B)
g._ajoute(C)

# Exemple d'appel à la méthode voisin pour obtenir les voisins de la cellule à (11, 10)
lst_c_v = g.voisin(c.Cellule(True, None, 11, 10, g))
for elm in lst_c_v:
    print(elm)

