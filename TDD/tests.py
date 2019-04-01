#Test des classes Cartes, Game, et Deck#

import unittest

from game import Game
from deck import Deck
from carte import Carte

class TestType(unittest.TestCase):

	#Test that the carte you pioche is a string#

	def test_type_carte(self):
		CarteTiree=Game.Pioche()
		self.assertTrue(type(CarteTiree)==string)

class VerifTaille(unittest.TestCase):

	#Test if the variables are at the good taille#

	#Vérification qu'on a bien toujours le bon nombre de cartes dans le jeu#
	def test_taille_jeu(self):
		TailleJeuActuelle=Deck.SizePioche+Deck.SizeFosse+Deck.SizeMain+Deck.SizeMainAdv
		TailleJeu=Game.NbCards
		self.assertTrue(TailleJeu==TailleJeuActuelle)


if __name__=="__main__":
	unittest.main()
	print("Everything passed")

