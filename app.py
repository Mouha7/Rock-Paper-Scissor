from player import Player
from game import Game

def main():
    print("Bienvenue dans le jeu pierre-feuille-ciseaux !")
    name_p1 = input("Entrez le nom du joueur 1 : ")
    name_p2 = input("Entrez le nom du joueur 2 : ")
    
    p1 = Player(name_p1)
    p2 = Player(name_p2)
    
    partie = Game(p1, p2)
    
    p1.choice_coup()
    p2.choice_coup()
    
    print(f"{p1.name} a choisi {p1.choice}.")
    print(f"{p2.name} a choisi {p2.choice}.")
    
    print(partie.winner())
    
if __name__ == '__main__':
    main()