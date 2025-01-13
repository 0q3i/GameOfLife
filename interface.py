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

#class config
class Config:

    def __init__(self,choix):
        self.choix = choix

    def choix_config(self,gr):
        if self.choix == "galder":
            self.glader(gr)
        elif self.choix == "cliniotant":
            self.cliniotant(gr)
        elif self.choix == "carre":
            self.carre(gr)

    def glader(self,gr):
        A = c.Cellule(True, None, 1, 1)
        B = c.Cellule(True, None, 2, 2)
        C = c.Cellule(True, None, 2, 3)
        D = c.Cellule(True, None, 1, 3)
        E = c.Cellule(True, None, 0, 3)
        gr.mat_ajoute(A)
        gr.mat_ajoute(B)
        gr.mat_ajoute(C)
        gr.mat_ajoute(D)
        gr.mat_ajoute(E)
    def cliniotant(self,gr):
        A = c.Cellule(True, None, 1, 1)
        B = c.Cellule(True, None, 1, 2)
        C = c.Cellule(True, None, 1, 3)
        gr.mat_ajoute(A)
        gr.mat_ajoute(B)
        gr.mat_ajoute(C)
    def carre(self,gr):
        A = c.Cellule(True, None, 1, 1)
        B = c.Cellule(True, None, 2, 1)
        C = c.Cellule(True, None, 1, 2)
        D = c.Cellule(True, None, 2, 2)
        gr.mat_ajoute(A)
        gr.mat_ajoute(B)
        gr.mat_ajoute(C)
        gr.mat_ajoute(D)


#class app pour tourner jeu
class App:

    def __init__(self,SCREEN_WIDTH,SCREEN_HEIGHT):
        px.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        px.run(self.update, self.draw)
        px.x= 0

    def update(self):
        self.x =(self.x + 1) % px.width


    def draw(self):
        px.cls(0)
        px.rect(self.x, 0, 8, 8, 9)
App(SCREEN_HEIGHT,SCREEN_WIDTH)

