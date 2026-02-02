def creer_grille() -> list:
    """
        Renvoie une liste de listes représentant
        un jeu de puissance 4 vide.
        Attention, le premier élément de la liste représente la ligne du haut !
        
        # Tests :
        >>> jeu = creer_grille()
        >>> len(jeu)
        6
        >>> len(jeu[0])
        7
    """
    pass

def afficher_grille(grille:list) -> None:
    """
        Affiche une grille de puissance 4
        Ne pas modifier !!!
    """
    res = '\n'
    
    for ligne in grille:
        res = res + '|' + '|'.join(ligne) + '|\n'
    
    res = res.replace(' ', chr(0x29BF))
    res = res.replace('J', chr(0x1F159))
    res = res.replace('R', chr(0x1F161))
    
    res = res + ' ' + 18*chr(0x203E) + '\n'
    print(res)
    
def jouer_jeton(grille:list, jeton:str, colonne:int) -> bool:
    """
        jeton : 'J' ou 'R'
        colonne : un entier entre 1 et 7
        retour : True si le jeton a pu être placé, False sinon
        
        Attention : il faut faire tomber le pion jusqu'à la première position disponible
    
        # Tests
        >>> jeu = creer_grille()
        >>> jouer_jeton(jeu, 'J', 1)
        True
        >>> jeu[5][0] == 'J'
        True
        >>> jouer_jeton(jeu, 'R', 1)
        True
        >>> jeu[4][0] == 'R'
        True
    """
    pass
    
def verifier_ligne(jeu:list, ligne:int) -> bool:
    """
        Vérifie si la ligne est gagnante
        ligne est un entier entre 1 et 6
        1 désigne la ligne du haut et 6 la ligne du bas
        
        # Tests :
        >>> jeu = creer_grille()
        >>> jeu[5] = ['J', 'J', 'R', 'J', 'J', 'J', 'J']
        >>> verifier_ligne(jeu, 1)
        False
        >>> verifier_ligne(jeu, 6)
        True
    """
    pass

def verifier_colonne(jeu:list, colonne:int) -> bool:
    """
        Vérifie si la colonne est gagnante
        colonne est un entier entre 1 et 7
        1 désigne la colonne de gauche et 7 la colonne de droite
        
        # Tests :
        >>> jeu = creer_grille()
        >>> jeu[0][2], jeu[1][2], jeu[2][2], jeu[3][2], jeu[4][2], jeu[5][2] = 'R', 'J', 'R', 'R', 'R', 'R'
        >>> verifier_colonne(jeu, 1)
        False
        >>> verifier_colonne(jeu, 3)
        True
    """
    pass

def verifier_diagonale_so_ne(jeu:list, diag:int) -> bool:
    """
        Vérifie si la diagonale SO-NE est gagnante
        diag est un entier entre 1 et 6 car il n'y a que 6 diagonales
        gagnantes possibles
        
        # Tests :
        >>> jeu = creer_grille()
        >>> jeu[5][0], jeu[4][1], jeu[3][2], jeu[2][3], jeu[1][4], jeu[0][5] = 'J', 'J', 'R', 'R', 'R', 'R'
        >>> verifier_diagonale_so_ne(jeu, 1)
        False
        >>> verifier_diagonale_so_ne(jeu, 3)
        True
    """
    pass
        
def verifier_diagonale_no_se(jeu:list, diag:int) -> bool:
    """
        Vérifie si la diagonale NO-SE est gagnante
        diag est un entier entre 1 et 6 car il n'y a que 6 diagonales
        gagnantes possibles
        
        # Tests :
        >>> jeu = creer_grille()
        >>> jeu[2][0], jeu[3][1], jeu[4][2], jeu[5][3] = 'J', 'J', 'J', 'J'
        >>> verifier_diagonale_no_se(jeu, 1)
        True
        >>> verifier_diagonale_no_se(jeu, 3)
        False
    """
    pass

def verifier_lignes(jeu:list) -> bool:
    """
        Vérifie toutes les lignes
    """
    pass

def verifier_colonnes(jeu:list) -> bool:
    """
        Vérifie toutes les colonnes
    """
    pass

def verifier_diagonales(jeu:list) -> bool:
    """
        Vérifie toutes les diagonales
    """
    pass

def grille_gagnante(jeu:list) -> bool:
    """
        Vérifie si une  grille est gagnante
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()