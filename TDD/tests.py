#Test des classes Cartes, Game, et Deck#

import unitest

class TestType(unitest.TestCase)

	def test_type_carte(CarteTiree):
		self.assertTrue(type(CarteTiree)==string), "Should be a string"

if __name__=="__main__":
	test_sum()
	print("Everything passed")

