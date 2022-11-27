from pile import Pile 

class Piquet:
    def __init__(self):
        self.piquet = Pile()
        
        
    def p_empiler(self, plateau):
        self.piquet.empiler(plateau)

        
    def p_depiler(self):
        return self.piquet.depiler()
    
    def p_dernier(self):
        return self.piquet.dernier()
        
    def est_vide(self):
        return self.piquet.est_vide()
        
    def __str__(self):
        return str(self.piquet)
    

        


class Jeu:
    def __init__(self,n):
        self.A = Piquet()
        self.B = Piquet()
        self.C = Piquet()
        for x in range(n):
            self.A.p_empiler(n-x)
            x = n-1
        print(self.A)
        print(self.B)
        print(self.C)
        
        
    def piquet_(self, numero):
        if numero == 1:
            return self.A
        if numero == 2:
            return self.B
        if numero == 3:
            return self.C  
    
    
    def deplace(self, depart, arriver):
        
        piquet_arriver = self.piquet_(arriver)
        piquet_depart = self.piquet_(depart)
        
        if not piquet_arriver.est_vide():
            if not piquet_arriver.p_dernier() > piquet_depart.p_dernier():
                return
        
        piquet_arriver.p_empiler(piquet_depart.p_dernier())
        piquet_depart.p_depiler()
        print(self.A)
        print(self.B)
        print(self.C)

    def gagner(self):
        if self.A.est_vide == True and self.B.est_vide == True :
            return True 
        else:
            return False 
 

# jeu.deplace(1, 3)
# jeu.deplace(1, 2)
# jeu.deplace(3,2)
# jeu.deplace(1,3)
# jeu.deplace(2,1)
# jeu.deplace(2,3)
# jeu.deplace(1,3)
