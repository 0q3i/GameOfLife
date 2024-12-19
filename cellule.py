from grille import voisin

class Cellule:
    def __init__(self, vivante, vivra, x, y, g):
        self.vivante = vivante
        self.vivra = vivra
        self.x = x
        self.y = y
        self.g = g

    def calcule_etat_futur(self):
        """Calcule l’état à venir de la cellule (attribut vivra), avec voisin et voisin_vivante"""
        #Recuper le tableau des voisins de la cellule self, lst_voisin
            #Avec voisins fournie par Grille, self.g.voisin(self)

        # Calcule le nb de cellule vivante. 
            #Avec la methode voisin_vivante, renvoie le nb de cellule vivante, renvoie nb_vivante (int). 

        #La methode future, verifie d'abord si self est vivante ou pas, avec nb_vivante.
            # Puis revoie un bool indiquand si la cellule vivra ou pas au prochaine tour. 

        #Avec future, on sait si la cellule vivra ou pas, alors on changera self.vivra en focntion.
            #If future():
                #self.vivra = True
            #else:
                #self.vivra = False
        pass
    
    def future(self, nb_vivante: int) -> bool :
        """Verifie en premier si self est vivante ou non.
        Verifie les regles du jeux, renvoie True ou False en fonction."""

        #Verifie d'abors si self.vivante == True:
            #If les nb_vivante sont moins que 2, alors return False
            #If les nb_vivante sont egale a 2 ou 3, alors return True
            #If les nb_vivante sont plus que 3, alors return False
        #Si self.vivante == False: 
            #If les nb_vivante sont egale a 3, alors return True
            #Else, return False
        pass


    def update(self):
        """Met à jour la cellule en affectant l’état à venir vivra à l’attribut actuel vivante"""
        self.vivante = self.vivra

    def voisin_vivante(self, voisin):
        """Renvoies le nombre de cellule vivante (int)"""
        #Utilise la methode voisin, class grille.
         #Parcour le tableau.
        #Verifie si chaque cellule est vivante, avec self.vivante == True
             #If True: ajoute +1 à nb_vivante
        #Renvoie a la fin de la boucle: nb_vivante
        pass

    def __str__(self):
        if self.vivante:
            return "+"
        else:
            return "-"
        
        

