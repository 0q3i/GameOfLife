from math import *
from cellule import *

class Grille:

    def __init__(self,l,h,lst_cellule):
        self.longuer = l #loguer d'une case
        self.hauteur = h #hauteur d'une case
        self.lst_c = lst_cellule #list des cellul vivante

    def grille(self):
        #desine une geille cet methode elle va pt pas excite dans le futur
        pass

    def tour(self):
        """ne renvois rien, modifi g dans la class cellul"""
        pass

    def rempilr(self):
        """revois un bool, s'il y a exactement 3 voisine la case devain vivante"""
        pass

    def voisin(self):
        """renvois un int, compte le nombre de voisin a une case donne"""
        voisin_tottale = -1
        for y in range(3):
            for x in range(3):
                pass

    def _ajoute(self, cellul):
        """renvois rein, elle ajoute les cellul vivante a lst_c"""
        self.lst_c.append(cellul)

    def _remove(self):
        """renvois rien, elle enleve les celluls de lst_c"""
        for i in range(len(self.lst_c)):
            if not self.lst_c[i].vivante:
                self.lst_c[i] = None
        self.lst_c = _nouv_lst(self.lst_c)
        
def _nouv_lst(lst):
    """renvois une nouvelle list avec que des cellul vivante, On suppose que la list est composer uniquement de cellul"""
    nouv_lst = [] 
    for elm in lst:
        if elm is not None:
            nouv_lst.append(elm)
    return nouv_lst
            