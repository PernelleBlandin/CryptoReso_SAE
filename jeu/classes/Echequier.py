from .Piece import Piece
from .Pion import Pion
from .Cavalier import Cavalier
from .Fou import Fou
from .Tour import Tour
from .Reine import Reine
from .Roi import Roi
import os

class Echiquier:
    pieces: list[Piece]

    def __init__(self):
        self.pieces = []
        self.initialiser_piece()

    def initialiser_piece(self):
        # Pions blancs
        for i in range(8):
            self.ajouter_piece(Pion(est_noir=False, position=(i, 1), mouvements_effectues=0))

        # Pions noirs
        for i in range(8):
            self.ajouter_piece(Pion(est_noir=True, position=(i, 6), mouvements_effectues=0))

        # Cavalier blancs
        self.ajouter_piece(Cavalier(est_noir=False, position=(1, 0), mouvements_effectues=0))
        self.ajouter_piece(Cavalier(est_noir=False, position=(6, 0), mouvements_effectues=0))

        # Cavalier noirs
        self.ajouter_piece(Cavalier(est_noir=True, position=(1, 7), mouvements_effectues=0))
        self.ajouter_piece(Cavalier(est_noir=True, position=(6, 7), mouvements_effectues=0))

        # Fou blancs
        self.ajouter_piece(Fou(est_noir=False, position=(2, 0), mouvements_effectues=0))
        self.ajouter_piece(Fou(est_noir=False, position=(5, 0), mouvements_effectues=0))

        # Fou noirs
        self.ajouter_piece(Fou(est_noir=True, position=(2, 7), mouvements_effectues=0))
        self.ajouter_piece(Fou(est_noir=True, position=(5, 7), mouvements_effectues=0))

        # Tour noirs
        self.ajouter_piece(Tour(est_noir=True, position=(0, 7), mouvements_effectues=0))
        self.ajouter_piece(Tour(est_noir=True, position=(7, 7), mouvements_effectues=0))

        # Tour blancs
        self.ajouter_piece(Tour(est_noir=False, position=(0, 0), mouvements_effectues=0))
        self.ajouter_piece(Tour(est_noir=False, position=(7, 0), mouvements_effectues=0))

        # Reine blanche
        self.ajouter_piece(Reine(est_noir=False, position=(3, 0), mouvements_effectues=0))

        # Reine noire
        self.ajouter_piece(Reine(est_noir=True, position=(3, 7), mouvements_effectues=0))

        # Roi blanc
        self.ajouter_piece(Roi(est_noir=False, position=(4, 0), mouvements_effectues=0))

        # Roi noir
        self.ajouter_piece(Roi(est_noir=True, position=(4, 7), mouvements_effectues=0))

    def ajouter_piece(self, piece: Piece):
        self.pieces.append(piece)

    # --- Méthodes utilitaires ---

    def get_piece(self, position: tuple[int, int]) -> Piece | None:
        """Retourne la pièce à une position donnée ou None si aucune pièce n'est présente
        Args:
            position (tuple[int, int]): la position à vérifier
        Returns:
            Piece | None: la pièce à la position donnée ou None si aucune pièce n'est présente
        """
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def est_vide(self, pos: tuple) -> bool:
        return self.get_piece(pos) is None

    def pos_valide(self, pos: tuple) -> bool:
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8

    # --- Logique de déplacement ---

    def __str__(self) -> str:
        """Affiche l'échiquier dans la console
        Returns:
            str: la représentation textuelle de l'échiquier
        """
        board_str = ""
        for y in range(7, -1, -1):
            board_str += f"{y+1} "
            for x in range(8):
                piece = self.get_piece((x, y))
                if piece:
                    board_str += f" {piece.stringRep} "
                else:
                    if (x + y) % 2 == 0:
                        board_str += " ☐ "
                    else:
                        board_str += " ■ "

            board_str += "\n"
        board_str += "   a  b  c  d  e  f  g  h \n"
        return board_str

    def recuperer_coups_possibles(self, piece: Piece) -> list[tuple[int, int]]:
        """Retourne tous les coups théoriquement possibles pour une pièce (sans vérifier l'échec)"""
        coups = []
        x, y = piece.position

        if isinstance(piece, Pion):
            dir_y = 1 if not piece.est_noir else -1
            # Avance de 1
            if self.pos_valide((x, y + dir_y)) and self.est_vide((x, y + dir_y)):
                coups.append((x, y + dir_y))
                # Avance de 2 (si premier mouvement)
                if piece.mouvements_effectues == 0 and self.pos_valide((x, y + 2*dir_y)) and self.est_vide((x, y + 2*dir_y)):
                    coups.append((x, y + 2*dir_y))
            # Captures diagonales
            for dx in [-1, 1]:
                target = (x + dx, y + dir_y)
                if self.pos_valide(target):
                    p = self.get_piece(target)
                    if p and p.est_noir != piece.est_noir:
                        coups.append(target)

        elif isinstance(piece, (Tour, Fou, Reine)):
            directions = []
            if isinstance(piece, (Tour, Reine)):
                directions.extend([(0, 1), (0, -1), (1, 0), (-1, 0)])
            if isinstance(piece, (Fou, Reine)):
                directions.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])
            
            for dx, dy in directions:
                for i in range(1, 8):
                    tx, ty = x + i*dx, y + i*dy
                    if not self.pos_valide((tx, ty)):
                        break
                    p = self.get_piece((tx, ty))
                    if p is None:
                        coups.append((tx, ty))
                    else:
                        if p.est_noir != piece.est_noir:
                            coups.append((tx, ty))
                        break # Bloqué par une pièce

        else: # Cavalier, Roi
            for dx, dy in piece.deplacements:
                tx, ty = x + dx, y + dy
                if self.pos_valide((tx, ty)):
                    p = self.get_piece((tx, ty))
                    if p is None or p.est_noir != piece.est_noir:
                        coups.append((tx, ty))
        
        return coups

    def est_en_echec(self, est_noir: bool) -> bool:
        """Vérifie si le roi de la couleur donnée est en échec"""
        roi_pos = None
        for p in self.pieces:
            if isinstance(p, Roi) and p.est_noir == est_noir:
                roi_pos = p.position
                break
        
        if not roi_pos:
            return False # Cas théorique impossible

        # Vérifier si une pièce adverse peut attaquer le roi
        for p in self.pieces:
            if p.est_noir != est_noir:
                # On récupère les coups "bruts" de l'adversaire
                coups = self.recuperer_coups_possibles(p)
                if roi_pos in coups:
                    return True
        return False

    def simuler_coup(self, piece: Piece, target: tuple) -> bool:
        """Simule un coup et retourne True si le coup est légal (ne met pas son propre roi en échec)"""
        original_pos = piece.position
        piece_capturee = self.get_piece(target)
        
        # Appliquer le coup
        if piece_capturee:
            self.pieces.remove(piece_capturee)
        piece.position = target
        
        # Vérifier l'échec
        en_echec = self.est_en_echec(piece.est_noir)
        
        # Annuler le coup
        piece.position = original_pos
        if piece_capturee:
            self.pieces.append(piece_capturee)
            
        return not en_echec

    def coups_legaux(self, est_noir: bool) -> list[tuple[Piece, tuple]]:
        """Retourne tous les coups légaux pour une couleur donnée"""
        coups = []
        for p in self.pieces:
            if p.est_noir == est_noir:
                possibles = self.recuperer_coups_possibles(p)
                for target in possibles:
                    if self.simuler_coup(p, target):
                        coups.append((p, target))
        return coups

    def deplacer(self, piece: Piece, pos: tuple):
        """Effectue le déplacement réel"""
        cible = self.get_piece(pos)
        if cible:
            self.pieces.remove(cible)
        piece.position = pos
        piece.mouvements_effectues += 1

    # --- Boucle de jeu ---

    def jouer(self):
        tour_noir = False # Les blancs commencent
        
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(self)
            
            joueur = "Noir" if tour_noir else "Blanc"
            print(f"C'est au tour des {joueur}s.")
            
            # Vérification Echec / Mat / Pat
            if self.est_en_echec(tour_noir):
                print(f"ECHEC aux {joueur}s !")
                if not self.coups_legaux(tour_noir):
                    print(f"ECHEC ET MAT ! Les {'Blancs' if tour_noir else 'Noirs'} gagnent !")
                    break
            else:
                if not self.coups_legaux(tour_noir):
                    print("PAT ! Match nul.")
                    break
            
            # Saisie du coup
            coup = input("Entrez votre coup (ex: e2e4) ou 'q' pour quitter: ").strip().lower()
            if coup == 'q':
                break
            
            if len(coup) != 4:
                input("Format invalide. Appuyez sur Entrée...")
                continue
                
            try:
                col_dep = ord(coup[0]) - ord('a')
                lig_dep = int(coup[1]) - 1
                col_arr = ord(coup[2]) - ord('a')
                lig_arr = int(coup[3]) - 1
                
                depart = (col_dep, lig_dep)
                arrivee = (col_arr, lig_arr)
                
                if not self.pos_valide(depart) or not self.pos_valide(arrivee):
                    input("Position hors du plateau. Appuyez sur Entrée...")
                    continue
                    
                piece = self.get_piece(depart)
                
                if not piece:
                    input("Pas de pièce à cette position. Appuyez sur Entrée...")
                    continue
                    
                if piece.est_noir != tour_noir:
                    input("Ce n'est pas votre pièce ! Appuyez sur Entrée...")
                    continue
                
                # Validation du coup
                coups_possibles = self.recuperer_coups_possibles(piece)
                if arrivee not in coups_possibles:
                    input("Coup impossible pour cette pièce. Appuyez sur Entrée...")
                    continue
                    
                if not self.simuler_coup(piece, arrivee):
                    input("Ce coup vous met en échec ! Appuyez sur Entrée...")
                    continue
                
                # Exécution
                self.deplacer(piece, arrivee)
                
                # Promotion du pion (simple: en Reine automatiquement)
                if isinstance(piece, Pion):
                    if (piece.est_noir and piece.position[1] == 0) or (not piece.est_noir and piece.position[1] == 7):
                        self.pieces.remove(piece)
                        self.ajouter_piece(Reine(piece.est_noir, piece.position, 0))
                        print("Promotion en Reine !")
                
                tour_noir = not tour_noir
                
            except ValueError:
                input("Erreur de format. Utilisez a-h et 1-8 (ex: e2e4). Appuyez sur Entrée...")
                continue
