class Pile:
    def __init__(self):
        self.pile = []
        
    def est_vide(self):
        if len(self.pile) == 0:
            return True 
        else:
            return False
    
    def empiler(self, element):
        self.pile.append(element)
    
        
    def depiler(self):
        return self.pile.pop()
       
    
    def dernier(self):
        if self.est_vide():
            return 9999
        return self.pile[-1]
        
    def taille(self):
        return len(self.pile)
    
    def __str__(self):
        return str(self.pile)