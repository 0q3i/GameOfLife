from math import *
from cellule import *
import pyxel as px


class Grille:

    def __init__(self,l,h,lst_cellule):
        self.longuer = l #longuer d'une case
        self.hauteur = h #hauteur d'une case
        self.lst_c = lst_cellule #list des cellul vivante

    def tour(self):
        """ne renvois rien, modifie g dans la class cellule pour pouvoir modifier la cellule"""
        #probleme je sais pas faire 
        pass
    
    def nombre_de_droitW(self,SCREEN_HIGHT):
        """Renvois int, calcul le nombre ce droit nessaire pour faire une grille"""
        #complexite constante
        return self.hauteur// SCREEN_HIGHT

    
    def nombre_de_droitH(self,SCREEN_WIGHT):
        """Renvois int, calcul le nombre ce droit nessaire pour faire une grille"""
        #complexite constante
        return self.longuer// SCREEN_WIGHT

    def voisin(self,cellule):
        """renvois une list de cellule, list de voisin de corrdonne x,y"""
        #la complexite est linaire car 3*3*n = 9n donc 9n operation
        lst_voisin = []
        for elm in self.lst_c:
            for y in range(3):
                for x in range(3):
                    if cellule.x + x == elm.x and cellule.y +y == elm.y:
                        lst_voisin.append(elm)
        return lst_voisin

    def _ajoute(self, cellule):
        """renvois rien, elle ajoute les cellules vivante a lst_c"""
        #complexite constante
        self.lst_c.append(cellule)

    def _remove(self):
        """renvois rien, elle enleve les cellules mortes de lst_c"""
        #complexite linaire car n operation
        for i in range(len(self.lst_c)):
            if not self.lst_c[i].vivante:
                self.lst_c[i] = None
        self.lst_c = _nouv_lst(self.lst_c)
        
def _nouv_lst(lst):
    """renvois une nouvelle list avec que des cellules vivantes.
      On suppose que lst est composer uniquement de cellules"""
    #complexite linaire n operation
    nouv_lst = [] 
    for elm in lst:
        if elm is not None: 
            nouv_lst.append(elm)
    return nouv_lst

#jeu de test





