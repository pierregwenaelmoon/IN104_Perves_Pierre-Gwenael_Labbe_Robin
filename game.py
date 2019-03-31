import random as rd
from carte import Carte


class Game(Carte):

    #Représente le jeu #

    def __init__(self):
        self.tas
        self.Name="Bataille"
        self.NbCards=2
        
        #Nombre de cartes à distribuer par joueur. Pour la bataille : toutes les cartes#
        self.NbCardsDistri=NbCards/2 

    def GetNbOfCards(self):
        return(NbCards)

    def GetTas(self):
        return(self.tas)

    def GetName(self):
            return(self.Name)

    def Pioche(self):
        tmp=rd.randint(0,1)
        piochee=self.tas[tmp]
        return([piochee,tmp])

    def Enleve(self,tmp):
        (self.tas).pop(tmp)   
