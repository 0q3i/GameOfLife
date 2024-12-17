import pyxel as px
import grille as g
import cellule as c

#les parametres
SCREEN_WIGHT = 1200
SCREEN_HIGHT = 1200

#class app pour tourner jeu
class App:

    def __init__(self,SCREEN_HIGHT,SCREEN_WIGHT):
        px.init(SCREEN_WIGHT, SCREEN_HIGHT)
        px.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pass

App(SCREEN_HIGHT,SCREEN_WIGHT)
