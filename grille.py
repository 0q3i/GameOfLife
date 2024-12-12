from math import *

class Grille:

    def __init__(self,l,h,lst_cellule):
        self.longuer = l #loguer d'une case
        self.hauteur = h #hauteur d'une case
        self.lst_c = lst_cellule #list des cellul vivante

    def tour(self):
        """ne renvois rien, modifi g dans la class cellul"""
        pass

    def rempilr(self):
        """revois un bool, s'il y a exactement 3 voisine la case devain vivante"""
        pass

    def voisin(self):
        """renvois un int, compte le nombre de voisin a une case donne"""
        pass

    def _ajoute(self):
        """renvois rein, elle ajoute les cellul vivante a lst_c"""
        pass

    def _remove(self):
        """renvois rien, elle enleve les celluls de lst_c"""
        pass