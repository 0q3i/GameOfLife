from math import *
import cellule as c

# Définition de la classe Grille qui représente la grille du jeu
class Grille:

    def __init__(self, x, y, l, h):
        """
        Inisilaisation 
        Paramètres :
        x : nombre de colonnes de la grille
        y : nombre de lignes de la grille
        """

        # Création de la matrice représentant la grille. Chaque cellule est une instance de Cellule
        # La grille est de taille x par y et chaque cellule est initialisée avec des valeurs par défaut
        # La Coordonnee 0 0 ce trouve toujour en haut a gauche
        self.matrice = [[c.Cellule(False, False, x_c, x_y) for x_c in range(x+1)] for x_y in range(y+1)]
        self.x = x
        self.y = y
        

    def tour(self):
        """
        Met à jour l'état de toutes les cellules de la grille.
        
        Cette méthode calcule l'état futur de chaque cellule et le met à jour.
        """

        for ligne in self.matrice:
            for c_colonne in ligne:
                c_colonne.calcule_etat_futur(self.voisin(c_colonne))
        for ligne in self.matrice:
            for c_colonne in ligne:
                c_colonne.update()


    def voisin(self, cellule):
        """
        Renvoie la liste des voisins d'une cellule.
        
        Paramètre :
        cellule : la cellule dont on souhaite trouver les voisins
        """
        lst_voisin = []
        for y in range(-1,2):
            for x in range(-1,2):
                if x == 0 and y == 0:
                    continue
                v_x=cellule.x+x
                v_y=cellule.y+y
                if 0<=v_y<=self.y and 0<=v_x<=self.x:
                    lst_voisin.append(self.matrice[v_y][v_x])
        return lst_voisin

    def mat_ajoute(self, cellule):
        """
        Ajoute une cellule vivante à la liste des cellules vivantes.
        
        Paramètre :
        cellule : la cellule vivante à ajouter à la liste
        """
        self.matrice[cellule.y][cellule.x]=cellule

    def mat(self):
        for lst in self.matrice:
            for elm in lst:
                print(elm, end = "|")
            print()