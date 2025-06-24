import pygame, time, random
pygame.init()
 
rect_x, rect_y = 100, 300
rect_speed_x, rect_speed_y = 5, 5
largeur, longueur, ligne, colonne = 700, 700, 28, 28
taille_case = largeur // 28
pomme_prise = False
screen = pygame.display.set_mode((longueur, largeur))
game_over_titre = pygame.font.Font(None, 70)
game_over_sous_titre = pygame.font.Font(None, 50)
score = pygame.font.Font(None, 16)
compteur_score = 0
pomme_recuperer=False
 
### Variables de couleurs
vert = (150, 245, 120)
noir = (0, 0, 0)
gris = (128, 128, 128)
vert_foncé = (0, 175, 76)
blanc = (255, 255, 255)
 
pomme = pygame.image.load("pomme.png")
pomme_resized = pygame.transform.scale(pomme, (25, 25))
 
direction = 0
 
rect_pos_x = 100
rect_pos_y = 350
Liste_rect=[pygame.Rect(rect_pos_x, rect_pos_y, 25, 25)]
 
 
running = True
 
pomme_nouvelle_position_x = 150
pomme_nouvelle_position_y = 350
rect_pomme = pygame.Rect(pomme_nouvelle_position_x, pomme_nouvelle_position_y, 25, 25)
 
def game_over():
   
    #------------------------------
   
    # Permet de mieux voir le lieu de mort.
    time.sleep(1)
   
    #--------------------------------
   
    screen.fill((102,192,230))
    screen.blit(game_over_titre.render("GAME OVER", True, noir), (200, 300))
    screen.blit(game_over_sous_titre.render(f"Votre score était de {compteur_score}", True, noir), (175, 345))
    pygame.display.flip()
    time.sleep(2)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_q:
                break
   
        break
#--------------- Ne marche pas-----------------
def restart_game():
    screen.fill(blanc)
    screen.blit("Game Over! Appuyez sur C pour rejouer ou Q pour quitter", noir)
    pygame.display.update()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_over()  # Relance une nouvelle partie
                    return
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
#-----------------------------------------------
pygame.display.set_caption("Snake")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_RIGHT:
                direction = 2
            if event.key == pygame.K_UP:
                direction = 3
            if event.key == pygame.K_DOWN:
                direction = 4
    if direction == 1:
        rect_pos_x -= 25
    if direction == 2:
        rect_pos_x += 25
    if direction == 3:
        rect_pos_y -= 25
    if direction == 4:
        rect_pos_y += 25
 
    ### Coloriage du fond
    for lignes in range(ligne):
        for colonnes in range(colonne):
            if (lignes + colonnes) % 2 != 0:
                couleur = vert
                pygame.draw.rect(screen, couleur, (colonnes * taille_case, lignes * taille_case, taille_case, taille_case))
            else:
                couleur = vert_foncé
                pygame.draw.rect(screen, couleur, (colonnes * taille_case, lignes * taille_case, taille_case, taille_case))
 
    ### Affiche du rectangle (ancien renne)
    New_list_rect=[pygame.Rect(rect_pos_x, rect_pos_y, 25, 25)]
    for rect in Liste_rect:
        New_list_rect.append(rect)
    if pomme_recuperer==False:
        New_list_rect.remove(Liste_rect[-1])
    Liste_rect = New_list_rect
    for rect in Liste_rect:
        pygame.draw.rect(screen,noir,rect)
   

    #------------------------------------------------
   
   ## Collision de la tête au mur
    tete=Liste_rect[0]
    if tete.left < -20 or tete.right > 720 or tete.top < -20 or tete.bottom > 720:
        game_over()
        running=False
        restart_game()
    #----------------------------------------------
   
   
   ## Collision du corps
    for segment in Liste_rect[1:]:
        if tete.colliderect(segment):
            game_over()  
            running=False
            restart_game()
    #----------------------------------------------
   
    ### Collision entre notre rectangle et nos objets
    if tete.colliderect(rect_pomme):
        pomme_prise = True
        compteur_score += 1
       
    if pomme_prise:
         
        #-------------------------------------------
       
        #Pour que la pomme apparaisse sur toute la grille
        position_x = random.randint(0, 27)
        position_y = random.randint(0, 27)
       
        #-------------------------------------------
       
        pomme_nouvelle_position_x = position_x * 25
        pomme_nouvelle_position_y = 25 * position_y
        rect_pomme = pygame.Rect(pomme_nouvelle_position_x, pomme_nouvelle_position_y, 25, 25)
        pomme_prise = False
        pomme_recuperer= True
    else:
        pomme_recuperer= False
    screen.blit(score.render(f"Votre score : {compteur_score} ", True, noir), (600, 0))
    screen.blit(pomme_resized, (pomme_nouvelle_position_x, pomme_nouvelle_position_y))
 
 
   
    time.sleep(0.1)
    pygame.display.flip()
pygame.quit()