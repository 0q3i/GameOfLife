
class Cellule:
    def __init__(self, vivante, vivra, x, y, g):
        self.vivante = vivante
        self.vivra = vivra
        self.x = x
        self.y = y
        self.g = g


    def calcule_etat_futur(self, voisin):
        """Calcule état à venir de la cellule (attribut vivra), avec voisin et voisin_vivante"""
        
        # Calcule le nb de cellule vivante. 
        nb_vivante = self.voisin_vivante(voisin)  # Appel à la méthode voisin_vivante pour compter les cellules vivantes
        
        # La méthode future, vérifie d'abord si self est vivante ou pas, avec nb_vivante.
        # Puis renvoie un bool indiquant si la cellule vivra ou pas au prochain tour.
        if self.future(nb_vivante):
            self.vivra = True
        else:
            self.vivra = False
    

    def future(self, nb_vivante: int) -> bool :
        """Verifie en premier si self est vivante ou non.
        Verifie les regles du jeux, renvoie True ou False en fonction."""
         # Verifie d'abord si self est vivante
        if self.vivante:
            if 2 <= nb_vivante <= 3:  # 2 ou 3 voisins vivants
                return True
            else: 
                return False
        else: 
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
            if v.vivante and v != voisin[(len(voisin)-1)//2]:  # Si la cellule voisine est vivante
                nb_vivante += 1  # Incrémente le compteur
        return nb_vivante  # Renvoie le nombre de cellules vivantes
    

    def __str__(self):
        if self.vivante:
            return "1" # Si la cellule est vivante, retourne "+"
        else:
            return "0" # Si la cellule est morte, retourne "-"

