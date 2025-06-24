import pygame, random, time, sys

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Gestion des collisions")


# police des texts
font_score= pygame.font.Font(None,30)
font_gameover=pygame.font.Font(None,100)
font_gameover_score=pygame.font.Font(None,70)


# Crée le rectangle du panier pour la collision
panier = pygame.Rect(100, 625, 150, 1)


# importer les images
image_panier = pygame.image.load('panier_ecureil.png')
image_resized_panier = pygame.transform.scale(image_panier, (150,110))
image_foret = pygame.image.load('foret.png')
image_resized_foret = pygame.transform.scale(image_foret, (1000,1000))

# les fruits
image_1 = pygame.image.load('banane.png')
image_B = pygame.transform.scale(image_1, (50, 50))

image_2 = pygame.image.load('pomme.png')
image_P = pygame.transform.scale(image_2, (50, 50))

image_3 = pygame.image.load('orange.png')
image_O = pygame.transform.scale(image_3, (50, 50))

image_4 = pygame.image.load('ananas.png')
image_A = pygame.transform.scale(image_4, (50, 50))

image_5 = pygame.image.load('citron.png')
image_C= pygame.transform.scale(image_5, (50, 50))

image_6 = pygame.image.load('Bombe.png')
image_Bombe = pygame.transform.scale(image_6, (50, 50))


#listes pour les charactéristique des fruits
Liste_fruits = [pygame.Rect(random.randint(30,550), 0, 50,50)]

Liste_image = [random.choice([image_B, image_P, image_O, image_A, image_C])]

List_value = [random.randint(100,300)]

list_bombe = [0]

rapiditee= float(0.002)


#initialisation du score
score = 0

# Paramètres du timer
heure_act_debut = pygame.time.get_ticks()  # Prend l'heure actuelle (en millisecondes)
duree_timer= 30000  # Durée du timer en millisecondes (par exemple, 5 secondes)

#Créer le fond (la forêt) hors de la boucle 
background = pygame.Surface((600, 800))
background.blit(image_resized_foret, (-250, -150))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Insérer l'image de fond
    screen.blit(background, (0, 0))


    # Calculer le temps écoulé depuis le début
    temps_ecoule = pygame.time.get_ticks() - heure_act_debut  # Temps écoulé en ms

    # Calculer le temps restant
    temps_restant = (duree_timer - temps_ecoule) // 1000  # En secondes

    # Affichage du temps restant
    screen.blit(font_score.render(f"Temps restant: {temps_restant}s", True, (255,140,0)), (200, 20))

    # Si le temps est écoulé
    if temps_ecoule >= duree_timer:
        screen.blit(font_gameover.render("Time's up !", True, (255,140,0)),(100, 750/2))
        screen.blit(font_gameover.render(f"score: {score} ", True, (255,140,0)),(100, 900/2))
        pygame.display.flip()
        time.sleep(5)
        running = False


    #permet de faire escendre le fruit et de les dessiner
    for k in range(len(Liste_fruits)):
        Liste_fruits[k].y += 1
        screen.blit((Liste_image[k]), (Liste_fruits[k]))
        
        #si le fruit atteint le nomdre random, il génère un nouveau fruit random
        if Liste_fruits[k].y==List_value[k]:
            new_fruit = pygame.Rect(random.randint(0,550), 0, 50,50)
            Liste_fruits.append(new_fruit)
            image_choisie = random.choice([image_B, image_P, image_O, image_A, image_C, image_Bombe, image_Bombe])
            Liste_image.append(image_choisie)
            if image_choisie == image_Bombe:
                list_bombe.append(1)
            else:
                list_bombe.append(0)
            new_value = random.randint(30,300)
            List_value.append(new_value)
            if rapiditee > 0.0001:
                rapiditee -= 0.0001
            
            #Réinitialiser les listes pour éviter le surplus d'éléments.
            if len(Liste_fruits)==100:
                New_Liste_fruits = [Liste_fruits[k] for k in range (71,100)]
                New_Liste_image = [Liste_image[k] for k in range (71,100)]
                New_List_value = [List_value[k] for k in range (71,100)]
                New_List_bombe = [list_bombe[k] for k in range (71,100)]
                Liste_fruits = New_Liste_fruits
                Liste_image = New_Liste_image
                List_value = New_List_value
                list_bombe = New_List_bombe

                
# Vérifier la collision entre les fruits et le panier
    for k in range(len(Liste_fruits)):
        if panier.colliderect(Liste_fruits[k]):
            

            #Changement de coordonnées pour éviter que le fruit repasse par sa valeur.
            #quand le fruits touche le panier il disparait
            Liste_fruits[k] = pygame.Rect(0, 1000, 0, 0)

            
            #si attrappe une bombe --> moins 20 points
            if list_bombe[k]==1:
                score -= 50
            #si attrappe un fruit --> plus 10 points
            else:
                score += 10
            

    # Déplacer le panier avec les touches fléchées
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        panier.x -= 1
    if keys[pygame.K_RIGHT]:
        panier.x += 1
    
    # empecher le panier de sortir
    if panier.x < 0:
        panier.x =  0
    if panier.x > 450:
        panier.x = 450
        
    # placer le panier
    screen.blit((image_resized_panier),panier)


    #afficher le score
    screen.blit(font_score.render(f"score: {score} ", True, (255,140,0)),(20,20))


    pygame.display.flip()
    time.sleep(rapiditee)

pygame.quit()
sys.exit()