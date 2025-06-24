import pygame, time, random, datetime
 
# initiation de pygame
pygame.init()
screen = pygame.display.set_mode((600, 650))
pygame.display.set_caption("PAC-MAN")

# l'ensemble des constantes et des variables
timer=0
rect_pacman = pygame.Rect(85,80,30,30)
rect_enemy1 = pygame.Rect(550,40,30,30)
rect_enemy2 = pygame.Rect(40,550,30,30)
rect_enemy3 = pygame.Rect(510,80,30,30)
rect_enemy4 = pygame.Rect(550,550,30,30)
rect_enemy5 = pygame.Rect(90,510,30,30)
font = pygame.font.Font(None, 70)
yellow = (252, 220, 18)
black = (0, 0, 0)
white = (255, 255, 255)
purple = (75, 0, 130)
red = (254, 27, 0)
cyan = (128, 208, 208)
image = pygame.image.load("LBJ.png")
img = pygame.image.load("ennemy.png")
pac_man = pygame.transform.scale(image,(30, 30))
pac_man_2 = pygame.transform.scale(image,(80, 80))
logo = pygame.image.load("ljp-2015-small.png")
logo_ljp = pygame.transform.scale(logo, (90, 30))
ennemy = pygame.transform.scale(img,(30, 30))
point_tp = pygame.Rect(570, 15, 16, 16)
img_pacman2 = pygame.image.load("pacman2.png")
img_pacman2_2 = pygame.transform.scale(img_pacman2, (250, 180))
largeur = 10
partie_commence = False
game_over = False
speed = 1
speed_rect3 = -1
speed_rect5 = 1

depart_temps = datetime.datetime.now()

liste_tp = [90, 190, 250, 400, 450, 50, 20]

# liste des murs
rect_liste = [
    pygame.Rect(50, 40, 125, largeur),
    pygame.Rect(50, 40, largeur, 125),
    pygame.Rect(425, 40, 125, largeur),
    pygame.Rect( 550, 40, largeur, 125),
    pygame.Rect( 550, 425, largeur, 125),
    pygame.Rect( 435, 550, 125, largeur),
    pygame.Rect( 50, 425, largeur, 125),
    pygame.Rect( 50, 550, 125, largeur),
    pygame.Rect(50, 250, largeur, 100),
    pygame.Rect( 550, 250, largeur, 100),  
    pygame.Rect( 250, 40, 100, largeur),
    pygame.Rect( 250, 550, 100, largeur),
    pygame.Rect( 135, 125, largeur, 350),
    pygame.Rect( 465, 125, largeur, 350),
    pygame.Rect( 215, 125, 180, largeur),
    pygame.Rect( 215, 465, 180, largeur),
    pygame.Rect( 145, 465, 10, largeur),
    pygame.Rect( 145, 125, 10, largeur),
    pygame.Rect( 455, 125, 10, largeur),
    pygame.Rect( 455, 465, 10, largeur), ]

# Fonction pour detecter les collisions avec le labyrinthe
def collide():
    collision=False
    for rect in rect_liste:
        if rect_pacman.colliderect(rect) :
            collision=True
    return collision
 
# Fonction pour le déplacement des ennemies 1, 2 et 4
def deplacement(ennemy, pos_x, pos_y):
    speed_ennemy = 1
    if pos_x >  ennemy.x  :          
            ennemy.x += speed_ennemy
    if pos_x <  ennemy.x  :
            ennemy.x -= speed_ennemy
    if pos_y > ennemy.y :
        ennemy.y += speed_ennemy
    if pos_y < ennemy.y :
        ennemy.y -= speed_ennemy

compteur =0
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



# presser espace pour commencer la partie
    keys = pygame.key.get_pressed()
    if not partie_commence and keys[pygame.K_SPACE]:
            partie_commence = True  
 
    if not partie_commence:
 
    # Texte du début
        screen.fill(cyan)
        font = pygame.font.Font(None, 40)
        font2 = pygame.font.Font(None, 24)
        text = font.render("Appuyez sur espace pour commencer", True, red)
        text2 = font2.render("Pac-Man game by Noa and Romain", True, black)
        screen.blit(text, (50, 240))
        screen.blit(text2, (160, 80))
        screen.blit(pac_man_2, (270, 125, 80, 80))
        screen.blit(logo_ljp, (500, 20, 90, 30))
           
 
    else:
        screen.fill(cyan)

    # bordure blanche en bas
        pygame.draw.rect(screen, white, (0, 600, 600, 50))

    # timer
        temps_ecoule = datetime.datetime.now() - depart_temps
        temps_ecoule_2 = int(temps_ecoule.total_seconds())

        font_temps = pygame.font.Font(None, 40)
        text_temps = font_temps.render(f"Timer :{temps_ecoule_2}s", True, red)
        screen.blit(text_temps, (235, 610))

    # position précédente
        pos_x, pos_y = rect_pacman.x, rect_pacman.y
    
    # création du labyrinthe
        for rect in rect_liste:
            pygame.draw.rect(screen, purple, rect)
    
    # création du personnage jouable
        screen.blit(pac_man, (rect_pacman))
        rect_x, rect_y = 30, 30
        
    # ennemies (5)
        screen.blit(ennemy, (rect_enemy1))
        timer +=1
        compteur +=1
        if compteur > 1500 :
            if timer == 3 :
                deplacement(rect_enemy2, pos_x, pos_y)
            screen.blit(ennemy, (rect_enemy2))
        
        if compteur > 3499 :
            if timer == 3 :
                deplacement(rect_enemy4, pos_x, pos_y)
            screen.blit(ennemy, (rect_enemy4))

        if timer == 5 :
            deplacement(rect_enemy1,pos_x,pos_y)
            timer=0

        screen.blit(ennemy, (rect_enemy3))
        rect_enemy3.x += speed_rect3
        if rect_enemy3.x > 515 :
            speed_rect3 = -speed_rect3
        if rect_enemy3.x  < 85 :
            speed_rect3 = -speed_rect3

            
        screen.blit(ennemy, (rect_enemy5))
        rect_enemy5.x += speed_rect5
        if rect_enemy5.x > 515 :
            speed_rect5 = -speed_rect5
        if rect_enemy5.x  < 85 :
            speed_rect5 = -speed_rect5


    # les 4 points de téléportations         
        tp1 = pygame.draw.rect (screen, red, (point_tp))
        tp2 = pygame.draw.rect (screen, red, (12, 570, 16, 16))
        tp3 = pygame.draw.rect (screen, red, (12, 12, 16, 16))
        tp4 = pygame.draw.rect (screen, red, (570, 570, 16, 16))

        if rect_pacman.colliderect(tp1) or rect_pacman.colliderect(tp2) or rect_pacman.colliderect(tp3) or rect_pacman.colliderect(tp4):
            rect_pacman.x = random.choice(liste_tp)
            rect_pacman.y = random.choice(liste_tp)
        

    # collision ennemis et pacman -> game over
        if rect_pacman.colliderect(rect_enemy1) or rect_pacman.colliderect(rect_enemy2) or rect_pacman.colliderect(rect_enemy3) or rect_pacman.colliderect(rect_enemy4) or rect_pacman.colliderect(rect_enemy5) :
            time.sleep(0.5)
            screen.fill(cyan)
            game_over = True
            font_gameover = pygame.font.Font("ComicSansMS.ttf", 24)
            font_gameover2 = pygame.font.Font(None, 24)
            text_gameover = font_gameover.render("Game Over!", True, red)
            text_gameover2 = font_gameover.render("Appuyer sur espace pour fermer!", True, black)
            centre = text_gameover.get_rect(center=(300, 300))

            temps_final = datetime.datetime.now() - depart_temps
            temps_final_2 = int(temps_final.total_seconds())

            font_temps_final = pygame.font.Font(None, 40)
            text_temps_final = font_temps_final.render(f"Votre temps était de {temps_final_2} secondes !", True, red)
            screen.blit(text_temps_final, (75, 160))

            screen.blit(text_gameover, centre)
            screen.blit(text_gameover2, (115, 75))
            screen.blit(img_pacman2_2,(160,300))
            pygame.display.flip()

    # appuyer sur espace ferme le jeu
            attente_game_over = True
            while attente_game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        attente_game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            running = False
                            attente_game_over = False
 
    # déplacement (W A S D)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            rect_pacman.x -= speed
        if keys[pygame.K_d]:
            rect_pacman.x += speed
        if keys[pygame.K_w]:
            rect_pacman.y -= speed
        if keys[pygame.K_s]:
            rect_pacman.y += speed
    
    # déplacement ( flèches )
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rect_pacman.x -= speed
        if keys[pygame.K_RIGHT]:
            rect_pacman.x += speed
        if keys[pygame.K_UP]:
            rect_pacman.y -= speed
        if keys[pygame.K_DOWN]:
            rect_pacman.y += speed
    
    
    # collisions avec les bords de la fenêtre
        if rect_pacman.x < 0 :
            rect_pacman.x = 0
        if rect_pacman.x > 570 :
            rect_pacman.x = 570
        if rect_pacman.y < 0 :
            rect_pacman.y = 0
        if rect_pacman.y > 570 :
            rect_pacman.y = 570
            

    # collisions avec les bords violets grace à une fonction
        if collide():
            rect_pacman.x = pos_x
            rect_pacman.y = pos_y
    
    pygame.display.flip()    
    time.sleep(0.004)
pygame.quit() 