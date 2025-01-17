import pyxel as px
import grille as g
import cellule as c

#les parametres
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
TAILLE_CELL = 10
GRILLE_CASE_LARGEUR = SCREEN_WIDTH // TAILLE_CELL
GRILLE_CASE_HAUTEUR = SCREEN_HEIGHT // TAILLE_CELL
GRILLE =g.Grille(GRILLE_CASE_LARGEUR,GRILLE_CASE_HAUTEUR)

# GRILLE.matrice[0][0].vivante = True

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
        elif self.choix == "cannon":
            self.cannon(gr)

    def glader(self,gr):
        A = c.Cellule(True, None, 5, 5)
        B = c.Cellule(True, None, 6, 6)
        C = c.Cellule(True, None, 4, 7)
        D = c.Cellule(True, None, 5, 7)
        E = c.Cellule(True, None, 6, 7)
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
        px.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Jeu de la Vie")
        self.g = GRILLE

        #Choisir la config
        while True:
            print("Les configurations possibles sont :")
            print("1. glader")
            print("2. cliniotant")
            print("3. carre")
            print("4. cannon")

            choix = input("Choisir une configuration : ").lower()

            if choix in ["glader", "cliniotant", "carre", "cannon"]:
                break
            else:
                print("Configuration invalide, veuillez réessayer.")

        self.config = Config(choix)
        self.config.choix_config(self.g)

        #lancer le jeu
        px.run(self.update, self.draw)

    def update(self):
        if px.btnp(px.KEY_Q):
            px.quit()
        if px.frame_count % 15 == 0:
            self.g.tour() 


    def draw(self):
        px.cls(7)

        for lst in self.g.matrice:
            for cell in lst:
                if cell.vivante:
                    c= 0
                else:
                    c= 7
                
                px.rect(
                    cell.x * TAILLE_CELL,
                    cell.y * TAILLE_CELL, 
                    TAILLE_CELL -1, 
                    TAILLE_CELL-1, 
                    c
                )
App(SCREEN_WIDTH, SCREEN_HEIGHT)

