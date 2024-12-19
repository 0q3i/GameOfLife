class Cellule:
    def __init__(self, vivante, vivra, x, y, g):
        self.vivante = vivante
        self.vivra = vivra
        self.x = x
        self.y = y
        self.g = g

    def calcule_etat_futur(self):
        """Calcule l’état à venir de la cellule (attribut vivra), avec voisin et voisin_vivante"""
        #Recuper le tableau des voisins de la cellule donner, lst_voisin
            #Avec voisins fournie par Grille, self.g.voisin(self)
        # Calculer le nb de cellule vivante, casses noires. 
            #Avec la methode voision_vivante
        #On aplique les regles pour savoir si oui ou non elle va etre vivante et on affect les resultas a vivra.
            #Si la cellule est entourer de moins 2 cases noires, elle meurt. Vivra = False
            #Si la cellule est entourer de 2 ou 3 cases noires, elle vie. Vivra = True
            #Si la cellule est entourer de plus de 3 cases noires, elle meurt. Vivra = False

        pass

    def update(self):
        """Met à jour la cellule en affectant l’état à venir vivra à l’attribut actuel vivante"""
        self.vivante = self.vivra

    def voisin_vivante(self):
        """Renvoies le nombre de casse noire (int)"""
        #Utilise la methode voisin, class grille.
         #parcourir le tableau, chaque cellule, et voir avec self.vivante is elle sont True
         #Si True alors .append dans liste
        pass

    def __str__(self):
        if self.vivante:
            return "+"
        else:
            return "-"
        
        

