import pygame, time

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600,800 ))
pygame.display.set_caption("Space Invaders")

# Objets
liste_ennemis = [[1 for k in range(9)] for j in range(4)] # Crée les ennemis dans un tableau de 1 
personnage = pygame.Rect(300, 720, 50, 25) # x, y, largeur, hauteur
canon = pygame.Rect(300, 700, 15, 30)
game_over_line = pygame.Rect(0, 680, 600, 5)

# Variables
game_over = True
running = True
restart_game = False

font1 = pygame.font.Font(None, 70) 
font2 = pygame.font.Font(None, 60) 
font3 = pygame.font.Font(None, 30) 

droite = 0
bas = 0
haut = 0

phase = 0
laser_position = canon.x
phase_laser = False

dernier_laser_temps = 0
cooldown = 0.25
cooldown_explosion = 0.05
temps_explosion = {}


bouton_restart = pygame.Rect(237, 399, 152, 39)
bouton_quit = pygame.Rect(237, 399, 95, 39)
bouton_quit2  = pygame.Rect(261,485, 95, 39)
selection = 0

start = False
demarage_unique = 0 


# Images
image_fond = pygame.image.load("fond.png")
image_fond_resized = pygame.transform.scale(image_fond, (600, 800))
screen.blit(image_fond_resized, (0,0))

image_personage = pygame.image.load("personage.png")
image_personage_resized = pygame.transform.scale(image_personage, (80, 60))
screen.blit(image_personage_resized, (120,140))

image_ennemis = pygame.image.load("ennemis.png")
image_ennemis_resized = pygame.transform.scale(image_ennemis, (48, 38))

image_explosion = pygame.image.load("explosion.png")
image_explosion_resized = pygame.transform.scale(image_explosion, (48, 35))


# Effet sonore & Musique
sons_explosion = pygame.mixer.Sound("explosion_ennemis.wav")
sons_explosion.set_volume(0.08)
pygame.mixer.music.load("musique.mp3")
pygame.mixer.music.play(-1)



while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Commence le jeu 
    if start :
        phase = 1
        phase_laser = True
        personnage.x = 300
        start = False
   

    # Variables
    victoire=True
    selection_restart = (255, 255, 255)
    selection_quit = (255, 255, 255)


    # Fond 
    screen.blit(image_fond_resized, (0,0))


    # Réinitialise le jeu
    if restart_game:
         game_over = True
         liste_ennemis = [[1 for i in range(9)] for i in range(4)]
         droite = 0 
         bas = 0
         phase = 1
         personnage.x = 300
         laser_position = canon.x
         temps_explosion = {}
         phase_laser = True
    if game_over:
         restart_game = False




    # Déplace le personage avec les touches fléchées
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        personnage.x -= 2.5
    if keys[pygame.K_RIGHT]:
        personnage.x  += 2.5
        
    if  personnage.left <= 0:
        personnage.x = 0
    if personnage.right >= 600:
        personnage.right = 600

    if keys[pygame.K_RETURN]:
        if demarage_unique == 0:
            start = True
            demarage_unique += 1

    canon.x = personnage.x + 15
    laser = pygame.Rect(laser_position + 2, 660 + haut, 7, 28)


    # Déplacement du laser et réinitialisation de sa position
    temps_maintenant = time.time() 
    if (temps_maintenant - dernier_laser_temps) >= cooldown: # Permet de mettre un temps d'attente entre chaque laser
        if phase_laser:
            haut -= 10
            if laser.top <= 0:
                haut += 1
                if laser.top == 0:
                    haut = 0
                    laser_position = canon.x
                    dernier_laser_temps = temps_maintenant
    


    
    # CREER UN RECTANGLE POUR CHAQUE VALEUR "1" DU TABLEAU. 
    liste_rect=[]
    for j in range(4):
        for k in range(9):
            if liste_ennemis[j][k]==1:
                rect=pygame.Rect(60*k + droite , 50*j+70 + bas , 40, 30)


                
                # S'IL Y A UNE COLLISION, LE "1" DEVIENT "0" ET LE RECTANGLE N'EST PAS AJOUTE DANS LA LISTE "VIVANTE".
                if rect.colliderect(laser):
                    sons_explosion.play()
                    laser_position = canon.x
                    liste_ennemis[j][k]=0
                    temps_maintenant = time.time() 
                    if (temps_maintenant - dernier_laser_temps) >= cooldown:
                        haut = 0
                        dernier_laser_temps = temps_maintenant
                else:
                    liste_rect.append(rect)
    

    # Regarde si le joueur a tiré sur tous les ennemis
    for j in range(4):
        for k in range(9):
            if liste_ennemis[j][k]==1:
                victoire=False

    if victoire==False:
        # CHERCHE LE RECTANGLE LE PLUS A GAUCHE.
        test_rect= True 
        k=0
        while test_rect:
            for j in range(4):
                if liste_ennemis[j][k]==1:
                    rect_gauche=pygame.Rect(60*k + droite , 50*j+70 + bas , 40, 30)
                    test_rect=False
                    break
            k=k+1
        
        # CHERCHE LE RECTANGLE LE PLUS A DROITE.
        test_rect= True
        k=8
        while test_rect:
            for j in range(4):
                if liste_ennemis[j][k]==1:
                    rect_droite=pygame.Rect(60*k + droite , 50*j+70 + bas , 40, 30)
                    test_rect=False
                    break
            k=k-1
        
        # CHERCHE LE RECTANGLE LE PLUS EN BAS
        test_rect= True
        j=3
        while test_rect:
            for k in range(9):
                if liste_ennemis[j][k]==1:
                    rect_bas=pygame.Rect(60*k + droite , 50*j+70 + bas , 40, 30)
                    test_rect=False
                    break
            j=j-1

        
        # Fait avancer les ennemis jusqu'à la ligne rouge, puis, si les ennemis ont touché le coin en bas à gauche, le jeu se met en Game over        
        if phase==1:
            if rect_droite.right <= 600: 
                droite += 0.5
            else:
                phase=2
        if phase==2:
            if rect_bas.bottom < 350:
                    bas += 0.5
            else:
                    phase=3
        if phase==3:
            if rect_gauche.left >= 0: 
                droite -= 0.5
            else:
                phase=4
        if phase==4:
            if rect_bas.bottom < 450:
                    bas += 0.5
            else:
                    phase=5
        if phase == 5:
            if rect_droite.right <= 600:
                droite += 0.5
            else:
                phase=6
        if phase==6:
            if rect_bas.bottom < 550:
                    bas += 0.75
            else:
                    phase=7
        if phase==7:
            if rect_gauche.left >= 0: 
                droite -= 0.75
            else:
                phase=8
        if phase==8:
            if rect_bas.bottom < 650:
                    bas += 0.80
            else:
                    phase=9
        if phase == 9:
            if rect_droite.right <= 600:
                droite += 0.80
            else:
                phase=10
        if phase==10:
            if rect_bas.bottom < 675:
                    bas += 0.82
            else:
                    phase=11
        if phase==11:
            if rect_gauche.left >= 0: 
                droite -= 0.82
            else:
                phase=12
        if phase ==12:
            game_over = False
            phase = 13
            phase_laser = False
        if phase == 13:
            pass




    # Affiche les objets
    pygame.draw.rect(screen, (255, 0, 0), game_over_line)
    pygame.draw.rect(screen, (0, 0, 0), canon)
    screen.blit(image_personage_resized, (personnage.x - 18, 700))
    


    # Affiche chaque ennemi encore vivant, puis affiche une explosion pendant 0.05 seconde pour chaque ennemi éliminé 
    for j in range(4):
        for k in range(9):
            if liste_ennemis[j][k]==1: # Si l'ennemi est vivant, afficher son image
                screen.blit(image_ennemis_resized, (60*k + droite , 50*j+70 + bas ))
            if liste_ennemis[j][k] == 0: #Si l'ennemi a été éliminé
                if (j, k) not in temps_explosion:  # Si l'explosion n'a pas été encore enregistrée pour cet ennemi
                    temps_explosion[(j, k)] = time.time()  # Enregistrer le temps de l'explosion pour l'ennemi éliminé dans un dictionnaire

                if time.time() - temps_explosion[(j, k)] < cooldown_explosion: # Affiche l'explosion pendant 0.05 seconde
                    screen.blit(image_explosion_resized, (60 * k + droite, 50 * j + 70 + bas))
        
    pygame.draw.rect(screen, (255, 0, 0), laser)

    

    # Menu de démarrage
    if demarage_unique == 0:
        screen.blit(image_fond_resized, (0,0))
        screen.blit(font1.render("Space Invaders", True, (255, 0, 0)), (128,300))
        screen.blit(font3.render("Par Janis et Arnaud", True, (255, 255, 255)), (200,350))
        screen.blit(font3.render("Appuyez sur << Entrée >> pour commencer", True, (255, 255, 255)), (100,500))
        screen.blit(font3.render("------------------------------------------------------", True, (255, 255, 255)), (125,525))
        screen.blit(font3.render("Utilisez les fléchées pour vous déplacer", True, (255, 255, 255)), (120,550))


    # Menu de Game over
    if selection == 1:
        selection_restart = (128, 128, 128)
    
    if selection == 0:
        selection_quit = (128, 128, 128)
    
    if game_over == False:
        screen.fill((0, 0, 0))
        screen.blit(font1.render("Game over", True, (255, 0, 0)), (175,300))
        pygame.draw.rect(screen, (selection_restart), bouton_restart, 2)
        screen.blit(font2.render("Restart", True, (selection_restart)), (240,400))
        screen.blit(font2.render("Quit", True, (selection_quit)), (265,485))
        pygame.draw.rect(screen, (selection_quit), bouton_quit2, 2)

        # Vérifie sur quel bouton la souris a été appuyé
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:  
            if bouton_restart.collidepoint(event.pos):  
                        restart_game = True
        if mouse[0]:  
            if bouton_quit2.collidepoint(event.pos):  
                        running = False
        # Vérifier la position de la souris et affiche le bouton sur lequel elle se trouve en blanc
        x, y = pygame.mouse.get_pos()

        if bouton_restart.collidepoint(x, y):
            selection = 0
        if bouton_quit2.collidepoint(x, y):
            selection = 1
        # Vérifie sur quel bouton la flèche est et affiche le bouton où elle se trouve en blanc
        if keys[pygame.K_UP]:
            selection = 0
        if keys[pygame.K_DOWN]:
            selection = 1
        if keys[pygame.K_RETURN]:
            if selection == 0:
                restart_game = True
            if selection == 1:
                running = False
        
            

    # Menu de Victoire
    if victoire:
        screen.fill((0, 0, 0))
        screen.blit(font1.render("You won !", True, (0, 255, 0)), (185,300))
        pygame.draw.rect(screen, (255, 255, 255), bouton_quit, 2)
        screen.blit(font2.render("Quit", True, (255, 255, 255)), (240,400))
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:  
            if bouton_restart.collidepoint(event.pos):  
                        running = False
        if keys[pygame.K_RETURN]:
            running = False
        
        

    pygame.display.flip()
    
    
    time.sleep(0.01)
pygame.quit()