from math import *
from cellule import *
import pyxel as px


class Grille:

    def __init__(self,l,h,lst_cellule):
        self.longuer = l #loguer d'une case
        self.hauteur = h #hauteur d'une case
        self.lst_c = lst_cellule #list des cellul vivante

    def tour(self):
        """ne renvois rien, modifi g dans la class cellul pour pouvoir modifier la cellul"""
        pass

    def voisin(self,cellule):
        """renvois un int, compte le nombre de voisin a une case donnee"""
        lst_voisin = []
        for y in range(3):
            for x in range(3):
                pass

    def _ajoute(self, cellule):
        """renvois rein, elle ajoute les cellul vivante a lst_c"""
        #complexite constante
        self.lst_c.append(cellule)

    def _remove(self):
        """renvois rien, elle enleve les celluls mort de lst_c"""
        #complexite linaire
        for i in range(len(self.lst_c)):
            if not self.lst_c[i].vivante:
                self.lst_c[i] = None
        self.lst_c = _nouv_lst(self.lst_c)
        
def _nouv_lst(lst):
    """renvois une nouvelle list avec que des cellul vivante, On suppose que lst est composer uniquement de cellul"""
    #complexite linaire
    nouv_lst = [] 
    for elm in lst:
        if elm is not None:
            nouv_lst.append(elm)
    return nouv_lst

#jeu de test