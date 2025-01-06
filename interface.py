#A faire lundi 7

import pyxel as px
import grille as g
import cellule as c

#les parametres
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
CELLULE_LARGEUR = 5
CELLULE_HAUTEUR = 5
GRILLE_CASE_LARGEUR = CELLULE_LARGEUR
GRILLE_CASE_HAUTEUR = CELLULE_HAUTEUR
GRILLE =g.Grille(GRILLE_CASE_LARGEUR,GRILLE_CASE_HAUTEUR,[])

#class app pour tourner jeu
class App:

    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT):
        px.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pass

App(SCREEN_HEIGHT,SCREEN_WIDTH)