class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
    
    def choice_coup(self):
        self.choice = input(f"{self.name} choisissez votre coup (Pierre[P], Feuille[F], Ciseau[C]) : ").lower()
        while self.choice not in ['pierre', 'feuille', 'ciseau', 'p', 'f', 'c']:
            print("Choix invalide. Veuillez choisir entre pierre, feuille ou ciseaux.")
            self.choice = input(f"{self.name}, veuillez choisir entre pierre, feuille ou ciseaux : ").lower()