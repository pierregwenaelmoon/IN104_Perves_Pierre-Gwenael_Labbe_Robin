#Test des classes Cartes, Game, et Deck#

import unittest

from game import Game

class TestType(unittest.TestCase):

	#Test that the carte you pioche is a string#

	def test_type_carte(self):
		CarteTiree=Game.Pioche()
		self.assertTrue(type(CarteTiree)==string), "Should be a string"

	
if __name__=="__main__":
	unittest.main()
	print("Everything passed")

