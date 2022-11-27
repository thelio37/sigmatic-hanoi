import pygame
import bouton
import hanoi

pygame.init()
n = 0
game_state = True

class Menu:
    def __init__(self) -> None:
        self.state_pygame = True
        self.nb_plateau = 5
        self.fond = pygame.image.load('assets/background.png')
        self.screen = pygame.display.set_mode((1080, 750))
        self.police = pygame.font.SysFont("Arial", 150)
        self.boutons = [bouton.Button(545, 600, (pygame.transform.scale(pygame.image.load("assets/haut.png").convert_alpha(), (150, 150))), self.screen),bouton.Button(385, 600, (pygame.transform.scale(pygame.image.load("assets/bas.png").convert_alpha(), (150, 150))), self.screen),bouton.Button(440, 250, (pygame.transform.scale(pygame.image.load("assets/start_btn.png").convert_alpha(), (200, 75))), self.screen)]
        
    def start(self):
        while self.state_pygame:
            global n, game_state
            
            self.screen.blit(self.fond, (0, 0))
            
            self.image_texte = self.police.render (str(self.nb_plateau), 1 , (0,0,0) )
            self.screen.blit(self.image_texte, (500, 50))
            
            for item in self.boutons:
                item.draw()
            
            for i in range(len(self.boutons)):
                if self.boutons[i].isClicked():
                    if i == 0:
                        self.nb_plateau += 1
                    elif i == 1:
                        self.nb_plateau -= 1
                    else: 
                        self.state_pygame = False
            
            if self.nb_plateau < 1:
                self.nb_plateau += 1
            elif self.nb_plateau > 9:
                self.nb_plateau -= 1
            
         
            n = self.nb_plateau      
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_state = False
                    self.state_pygame = False
                     

            pygame.display.update() 


class Interface:
    def __init__(self, n):
        """
        Initialise une interface pour jouer au Tour de Hanoi.
        @:param: n Le nombre de plateaux sur le jeu.
        """
        self.jeu = hanoi.Jeu(n)
        self.n = n 
        self.font = pygame.font.SysFont('Arial', 40)
        self.fond = pygame.image.load('assets/background.png')
        self.state_pygame = True
        self.plateaux = []
        self.screen = pygame.display.set_mode((1080, 750))
        pygame.display.set_caption('Most Sigmatic Game of 2022')
        pygame.time.Clock().tick(10)
        self.screen.blit(self.fond, (0, 0))
        self.musique = True
        self.son = pygame.mixer.music.load("assets/musique.mp3")

        # Création des boutons
        self.boutons = [bouton.Button(60, 600, (pygame.transform.scale(pygame.image.load("assets/1_2.png").convert_alpha(), (125, 75))), self.screen), bouton.Button(60, 680, (pygame.transform.scale(pygame.image.load("assets/1_3.png").convert_alpha(), (125, 75))), self.screen), bouton.Button(480, 600, (pygame.transform.scale(pygame.image.load("assets/2_1.png").convert_alpha(), (125, 75))), self.screen), bouton.Button(480, 680, (pygame.transform.scale(pygame.image.load("assets/2_3.png").convert_alpha(), (125, 75))), self.screen), bouton.Button(890, 600, (pygame.transform.scale(pygame.image.load("assets/3_1.png").convert_alpha(), (125, 75))), self.screen), bouton.Button(890, 680, (pygame.transform.scale(pygame.image.load("assets/3_2.png").convert_alpha(), (125, 75))), self.screen)]


    def afficher_plateau(self):
        """
        Permet d'afficher les plateaux sur la fenetre.
        """
        for i in range(len(self.jeu.A.piquet.pile)):
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(110, 600 - 30 * self.n + 30 * i, 30 * self.jeu.A.piquet.pile[len(self.jeu.A.piquet.pile)-i-1], 20))
        for i in range(len(self.jeu.B.piquet.pile)):
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(540, 400 - 30 * self.n + 30 * i, 30 * self.jeu.B.piquet.pile[len(self.jeu.B.piquet.pile)-i-1], 20))
        for i in range(len(self.jeu.C.piquet.pile)):
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(940, 600 - 30 * self.n + 30 * i, 30 * self.jeu.C.piquet.pile[len(self.jeu.C.piquet.pile)-i-1], 20))


    def start(self):
        """
        Permet de lancer le jeu.
        """
        while self.state_pygame:
            
            #pygame.mixer.music.load("images musique/Darude - Sandstorm.mp3")
            self.screen.blit(self.fond, (0, 0))
            #self.musique
            if self.musique:
                pygame.mixer.music.play(100)
                self.musique = False

            # Affichage des piquets
            for i in range(3):
                if i == 0:
                    x = 110
                if i == 1:
                    x = 540
                if i == 2:
                    x = 940
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x, 150 if i == 1 else 355, 20, 250))
                
            # affiche les boutons
            for item in self.boutons:
                item.draw()

            # vérifie l'état du clic pour chaque bouton
            for i in range(len(self.boutons)):
                if self.boutons[i].isClicked():
                    correspondance_btn = {
                        0: (1, 2),
                        1: (1, 3),
                        2: (2, 1),
                        3: (2, 3),
                        4: (3, 1),
                        5: (3, 2)
                    }
                    self.jeu.deplace(correspondance_btn[i][0], correspondance_btn[i][1])
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state_pygame = False
            self.afficher_plateau()
            
            if self.jeu.gagner() == True:
                print("cool")

            pygame.display.update()

menu = Menu()
menu.start()

if game_state:
    game = Interface(n)
    game.start()
