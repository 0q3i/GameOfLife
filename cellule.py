from grille import voisin

class Cellule:
    def __init__(self, vivante, vivra, x, y, g):
        self.vivante = vivante
        self.vivra = vivra
        self.x = x
        self.y = y
        self.g = g


    def calcule_etat_futur(self):
        """Calcule état à venir de la cellule (attribut vivra), avec voisin et voisin_vivante"""
       # Recuper le tableau des voisins de la cellule self, lst_voisin
        lst_voisin = self.g.voisin(self)  # Appel à la méthode voisin de la classe Grille

        # Calcule le nb de cellule vivante. 
        nb_vivante = self.voisin_vivante(lst_voisin)  # Appel à la méthode voisin_vivante pour compter les cellules vivantes

        # La méthode future, vérifie d'abord si self est vivante ou pas, avec nb_vivante.
        # Puis renvoie un bool indiquant si la cellule vivra ou pas au prochain tour.
        if self.future(nb_vivante):
            self.vivra = True
        else:
            self.vivra = False
    

    def future(self, nb_vivante: int) -> bool :
        """Verifie en premier si self est vivante ou non.
        Verifie les regles du jeux, renvoie True ou False en fonction."""
         # Verifie d'abord si self.vivante == True:
        if self.vivante:
            if nb_vivante < 2:  # Moins de 2 voisins vivants
                return False
            elif nb_vivante == 2 or nb_vivante == 3:  # 2 ou 3 voisins vivants
                return True
            else:  # Plus de 3 voisins vivants
                return False
        else:  # Si self.vivante == False
            if nb_vivante == 3:  # Exactement 3 voisins vivants
                return True
            else:
                return False


    def update(self):
        """Met à jour la cellule en affectant état à venir vivra à attribut actuel vivante"""
        self.vivante = self.vivra


    def voisin_vivante(self, voisin):
        """Renvoies le nombre de cellule vivante (int)"""
       # Utilise la méthode voisin, classe Grille.
        nb_vivante = 0  # Initialisation du compteur de cellules vivantes
        for v in voisin:  # Parcours du tableau des voisins
            if v.vivante:  # Si la cellule voisine est vivante
                nb_vivante += 1  # Incrémente le compteur
        return nb_vivante  # Renvoie le nombre de cellules vivantes
    

    def __str__(self):
        if self.vivante:
            return "+" # Si la cellule est vivante, retourne "+"
        else:
            return "-" # Si la cellule est morte, retourne "-"
        
        

