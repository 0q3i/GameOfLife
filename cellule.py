class Cellule:
    def __init__(self, vivante, vivera, x, y, g):
        self.vivante = vivante
        self.vivera = vivera
        self.x = x
        self.y = y
        self.g = g

    def calcule_etat_futur():
        """Calcule l’état à venir de la cellule (attribut vivra), avec voisin et voisin_vivante"""
        pass

    def update(self):
        """Met à jour la cellule en affectant l’état à venir vivra à l’attribut actuel vivante"""
        self.vivante = self.vivra

    def voisin_vivante():
        """Revoies le nombre de casse noire renvois un int, compte le nombre de voisin vivant a une case donnee"""
        pass

    def rempilr(self):
        """revois un bool, s'il y a exactement 3 voisine vivant la case devain vivante"""
        pass