import pyxel as px
import grille as g
import cellule as c

#les parametres
SCREEN_WIDTH = 100
SCREEN_HEIGHT = 100
TAILLE_CELL = 8
GRILLE_CASE_LARGEUR = 10
GRILLE_CASE_HAUTEUR = 10
GRILLE =g.Grille(GRILLE_CASE_LARGEUR,GRILLE_CASE_HAUTEUR)
GRILLE.matrice[0][0].vivante = True
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
        self.x = SCREEN_WIDTH

    def update(self):
        pass



    def draw(self):
        px.cls(0)
        for lst in GRILLE.matrice:
            for cell in lst:
                if cell.vivante:
                    c= 0
                else:
                    c= 7
                
                px.rect(cell.x * TAILLE_CELL, cell.y * TAILLE_CELL, TAILLE_CELL, TAILLE_CELL, c)
App(SCREEN_HEIGHT,SCREEN_WIDTH)

