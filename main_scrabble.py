
def get_dictionnaire(choix="français"):
    # TO DO (ouvrir un fichier, le lire, convertir en ensemble python de strings)
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
    
    - nb_tuiles_chevalet: le nombre de tuiles présentes sur le chevalet
    - liste_tuiles : liste des tuiles sur le chevalet.                # maybe c'est mieux d'implémenter avec un dict : Tuile: nb occurences de cette tuile mais en vrai osef je pense.
    """



class Scrabble():
    """
    Classe encodant l'état complet jeu.
    
    Variables & Constantes contenus :
        
    - DICTIONNAIRE : ensemble python de strings formant les mots du dictionnaire authorisé.
        
    - TAILLE = (n,m) couple nb lignes/colonnes
    - grille_lettres : matrice numpy de taille nxm contenant une Tuile ou None si la case est vide
    - GRILLE_MODIFS : matrice numpy de taille nxm contenant ("MULT_LETTRE",k) ou ("MULT_MOT",k) ou None sinon
    
    - NB_TUILES_INITIAL
    - nb_tuiles_sac 
    
    - TUILES_INITIALES : liste de NB_TUILES_INITIAL Tuiles
    - tuiles_sacs : liste de nb_tuiles_sac Tuiles, celles contenues dans le sac
    
    - NB_JOUEURS (seront numérotés de 0 à NB_JOUEURS - 1)
    - prochain_joueur
    
    - TUILES_MAX_CHEVALET
    - chevalets : liste de NB_JOUEURS Chevalets
    
    - NB_POINTS_SCRABBLE: le nombre de points bonus obtenus en réalisant un Scrabble.
    
    
    Fonctions contenus : 
    
    - est_legal(coup): renvoie True/False selon si le coup joué est légal (pour le jouer à qui c'est le tour de jouer, donc)
    """ 
    
    
    
class Coup():
    """
    classe encodant une tentative de coup à jouer (pas forcément légal)
    
    - placements = liste de tuples (Tuile,(i,j))
    """
    
    
def joue(scrabble:Scrabble, coup:Coup):
    # renvoie le nouvel état du jeu après le coup joué (si le coup est illégal, renvoie une erreur avec Assert "coup illégal")
    pass
    
    
    
    
    
    
    
    
    
    
    
# maybe déplacer ces fonctions etc dans un autre fichier à la fin, mais je pense que c'est mieux de la mettre au même endroit pour le début
def calculs_initiaux():
    pass
    
    
def calcul_meilleurs_coups(scrabble,res_initiaux):
    """
    On s'autorise à garder des calculs faits initialement (ex: transformer le dict en une autre structure) une seule fois. 
    On pourrait aussi stocker des calculs précédents intermédiaires des coups précédents mais je crois pas que ça serait utile.
    
    """
    
    
    
    
    
    
    
