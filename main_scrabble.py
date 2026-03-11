
def get_dictionnaire(choix="français"):
    # TO DO
    pass


def scrabble_initial_standard() :
    #TO DO
    DICTIONNAIRE = get_dictionnaire("français")
    NB_LIGNES, NB_COLONNES = 15,15
    ...

    return Scrabble(...)




class Tuile():
    """
    classe tuile représentant entièrement une tuile :
        
    - symbole : ex: "B"," " pour un joker
    - valeur : ex: 3
    """
    
class Chevalet():
    """
    classe Chevalet représentant 
    """



class Scrabble():
    """
    Classe encodant l'état complet jeu.
    
    Variables contenu :
        
    - TAILLE = (n,m) couple nb lignes/colonnes
    - grille_lettres : matrice numpy de taille nxm contenant une Tuile ou None si la case est vide
    - GRILLE_MODIFS : matrice numpy de taille nxm contenant ("MULT_LETTRE",k) ou ("MULT_MOT",k) ou ('',0) sinon
    
    - NB_TUILES_INITIAL
    - nb_tuiles_sac 
    
    - TUILES_INITIALES : liste de NB_TUILES_INITIAL Tuiles
    - tuiles_sacs : liste de nb_tuiles_sac Tuiles, celles contenues dans le sac
    
    - NB_JOUEURS (seront numérotés de 0 à NB_JOUEURS - 1)
    - prochain_joueur
    
    - chevalets : liste de NB_JOUEURS Chevalets
    
    
    
    
    
    
    
    """ 
    
