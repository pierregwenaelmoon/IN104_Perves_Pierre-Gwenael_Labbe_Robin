import random as rd
from game import Game


class Deck(Game):

    #Représente les mains et la fosse#
    
    def __init__(self):
        Game.__init__(self)
        
        #Cartes restantes dans la pioche#
        self.NbCardsPioche=self.GetNbOfCards()
        self.Pioche=[]
        
        self.Main=[]
        self.SizeMain #Nb de cartes dans la main#
        
        self.Fosse=[]
        self.SizeFosse
        
        self.MainAdv=[] #Main de l'adversaire#
        self.SizeMainAdv 

    
    #On distribue les cartes#
    def Distribuer(self,NbCardsDistri):
        self.Main
        
    def GetMain(self):
        return(self.Main)
    
    def GetMainAdv(self):
        return(self.MainAdv)
    
    def GetFosse(self):
        return(self.Fosse)

    def AddMain(self,carte):
        (self.Main).append(carte)
        self.SizeMain+=1

    def AddMainAdv(self,carte):
        (self.MainAdv).append(carte)
        self.SizeMainAdv+=1

        
    def AddFosse(self,carte):
        (self.Fosse).append(carte)
        self.SizeFosse+=1

    def UpdatePioche(self):
        self.NbCardsPioche-=1

    #Retirer une carte de la main#
        
    def TakeOffMain(self,carte):  
        pos=(self.Main).index(carte)
        (self.Main).pop(pos)
        self.SizeMain-=1
        
    #Retirer une carte de la main de l'adversaire#
        
    def TakeOffMainAdv(self,carte):
        pos=(self.MainAdv).index(carte)
        (self.MainAdv).pop(pos)
        self.SizeMainAdv-=1
        
    #Retirer une carte de la pioche#
        
    def TakeOffPioche(self,carte):
        pos=(self.Pioche).index(carte)
        (self.Pioche).pop(pos)
        self.SizeMainAdv-=1
      
    

    
        



    

    
    
