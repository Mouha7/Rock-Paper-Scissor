class Game:
    def __init__(self, player_one, player_two):
        self.p1 = player_one
        self.p2 = player_two
    
    def winner(self):
        if self.p1.choice == self.p2.choice:
            return "Égalité !"
        elif (self.p1.choice == 'pierre' and self.p2.choice == 'ciseaux') or \
            (self.p1.choice == 'feuille' and self.p2.choice == 'pierre') or \
            (self.p1.choice == 'ciseaux' and self.p2.choice == 'feuille') or \
            (self.p1.choice == 'p' and self.p2.choice == 'c') or \
            (self.p1.choice == 'f' and self.p2.choice == 'p') or \
            (self.p1.choice == 'c' and self.p2.choice == 'f'):
            return f"{self.p1.name} a gagné !"
        else:
            return f"{self.p2.name} a gagné !"