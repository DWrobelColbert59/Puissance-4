"""
    Puissance 4 : Les règles du jeu
    
    Le but du jeu est d'aligner une suite de 4 pions
    de même couleur sur une grille comptant 6 rangées et 7 colonnes.
    Chaque joueur dispose de 21 pions d'une couleur (par
    convention, en général jaune ou rouge). Tour à tour, les deux
    joueurs placent un pion dans la colonne de leur choix, le pion
    coulisse alors jusqu'à la position la plus basse possible dans
    ladite colonne, à la suite de quoi c'est à l'adversaire de jouer.
    Le vainqueur est le joueur qui réalise le premier un alignement
    (horizontal, vertical ou diagonal) consécutif d'au moins quatre
    pions de sa couleur. Si, alors que toutes les cases de la grille
    de jeu sont remplies, aucun des deux joueurs n'a réalisé un tel
    alignement, la partie est déclarée nulle.
"""

if __name__ == "__main__":
    
    from grid import *
    jeu = creer_grille()
    afficher_grille(jeu)
    
    joueur = 'J'
    
    while not grille_gagnante(jeu):
        c = int(input(f"Joueur {joueur} : Quelle colonne souhaitez-vous jouer ? "))
        
        while jouer_jeton(jeu, joueur, c) == False:
            print("La colonne est pleine.\n")
            c = int(input(f"Joueur {joueur} : Quelle colonne souhaitez-vous jouer ? "))
        
        afficher_grille(jeu)
        
        if joueur == 'J':
            joueur = 'R'
        else:
            joueur = 'J'
    