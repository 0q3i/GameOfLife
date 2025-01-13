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
    def cannon(self,gr):
        lst_pos= [(1,15),(2,15),(1,16),(2,16),(11,15),(11,16),(11,14),(12,13),
              (13,12),(14,12),(12,17),(13,18),(14,18),(15,15),(16,13),(17,14),
              (17,15),(18,15),(17,16),(16,17),(21,16),(22,16),(21,17),(22,17),
              (21,18),(22,18),(23,15),(25,15),(25,14),(23,19),(25,19),(25,20),
              (39,18),(40,18),(39,17),(40,17)
              ]
        for elm in lst_pos:
            A = c.Cellule(True,None,elm[0],elm[1])
            gr.mat_ajoute(A)



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