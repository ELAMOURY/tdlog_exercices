"""
We want to have a new class Item such as :

A new item can be created with Item(price, weight)
    The price and weight of an item can be accessed with
    item.price and item.weight.
    Write the code for this class, with the appropriate constructor.
Example of code using the class: i = Item(10, 20)
"""
class Item:
    def __init__(self, price, weight):
        # Constructeur : initialise les attributs de prix et de poids
        self.price = price
        self.weight = weight
    
    def afficher_info(self):
        # Méthode pour afficher les informations de l'objet
        print(f"Prix : {self.price}, Poids : {self.weight}")

# Exemple d'utilisation de la classe
i = Item(10, 20)
i.afficher_info()  # Affiche : Prix : 10, Poids : 20
