#import et initialisation des différents paramètres ou variables
import pygame, time, random, os
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("fenetre de jeu")
font = pygame.font.Font(None, 70)
font_regles = pygame.font.Font(None, 40)
font_regles_titre = pygame.font.Font(None, 70)
font_regles_titre.set_underline(True)
yellow=(255,255,0)
blue=(0,0,200)
song1='levels.wav'
song2='champion.mp3'
song3='chanson.mp3'
restart= False
#collision entre le rectangle rouge (un des décapsuleurs) et la liste:
def collide():
        collision=False
        for rect in rect_List:
            if rectrouge.colliderect(rect):
                collision=  True
        return collision
        
#collision entre le rectangle bleu (l'autre des décapsuleurs) et la liste:
def collideblue():
    collision=False
    for rect in rect_List:
        if rectbleu.colliderect(rect):
            collision= True
        
    return collision
#collision entre le bouton bleu (la bière) et la liste
def collidebutton():
    collision=False
    for rect in rect_List:
        if button.colliderect(rect):
            collision= True
        
    return collision


#liste de rectangles formant les murs:
ligne=79
rect_List = [
    pygame.Rect(0, 0, 800, 10),       # Bord supérieur
    pygame.Rect(0, 0, 10, 800),       # Bord gauche
    pygame.Rect(790, 0, 10, 800),     # Bord droit
    pygame.Rect(0, 790, 800, 10),     # Bord inférieur
    pygame.Rect(10+ligne*0,10+ligne*2, ligne*2, 10),
    pygame.Rect(10+ligne*2,10+ligne*1, ligne*1, 10),
    pygame.Rect(10+ligne*1,10+ligne*3, ligne*2, 10),
    pygame.Rect(10+ligne*1,10+ligne*4, ligne*1, 10),
    pygame.Rect(10+ligne*2,10+ligne*5, ligne*3, 10),
    pygame.Rect(10+ligne*1,10+ligne*6, ligne*2, 10),
    pygame.Rect(10+ligne*2,10+ligne*8, ligne*3, 10),
    pygame.Rect(10+ligne*2,10+ligne*9, ligne*2, 10),
    pygame.Rect(10+ligne*4,10+ligne*7, ligne*1, 10),
    pygame.Rect(10+ligne*4,10+ligne*6, ligne*2, 10),
    pygame.Rect(10+ligne*4,10+ligne*2, ligne*1, 10),
    pygame.Rect(10+ligne*6,10+ligne*1, ligne*1, 10),
    pygame.Rect(10+ligne*6,10+ligne*3, ligne*2, 10),
    pygame.Rect(10+ligne*9,10+ligne*1, ligne*1, 10),
    pygame.Rect(10+ligne*7,10+ligne*4, ligne*2, 10),
    pygame.Rect(10+ligne*9,10+ligne*5, ligne*1, 10),
    pygame.Rect(10+ligne*8,10+ligne*8, ligne*1, 10),
    pygame.Rect(10+ligne*6,10+ligne*8, ligne*1, 10),
    pygame.Rect(10+ligne*2,10+ligne*1,10, ligne*1),
    pygame.Rect(10+ligne*3,10+ligne*1,10, ligne*2),
    pygame.Rect(10+ligne*1,10+ligne*3,10, ligne*1),
    pygame.Rect(10+ligne*4,10+ligne*3,10, ligne*2),
    pygame.Rect(10+ligne*4,10+ligne*1,10, ligne*1),
    pygame.Rect(10+ligne*5,10+ligne*0,10, ligne*2),
    pygame.Rect(10+ligne*6,10+ligne*0,10, ligne*1),
    pygame.Rect(10+ligne*1,10+ligne*6,10, ligne*3),
    pygame.Rect(10+ligne*3,10+ligne*6,10, ligne*1),
    pygame.Rect(10+ligne*4,10+ligne*9,10, ligne*1),
    pygame.Rect(10+ligne*5,10+ligne*7,10, ligne*2),
    pygame.Rect(10+ligne*6,10+ligne*8,10, ligne*2),
    pygame.Rect(10+ligne*6,10+ligne*3,10, ligne*4),
    pygame.Rect(10+ligne*8,10+ligne*0,10, ligne*2),
    pygame.Rect(10+ligne*7,10+ligne*4,10, ligne*2),
    pygame.Rect(10+ligne*9,10+ligne*1,10, ligne*2),
    pygame.Rect(10+ligne*8,10+ligne*5,10, ligne*4),
    pygame.Rect(10+ligne*9,10+ligne*5,10, ligne*3)
    
]
#importation des fichiers images et musique :
image1=pygame.image.load("decapsuleur.jpg")
image2=pygame.image.load("biere.jpg")
image3=pygame.image.load("eau.webp")
image4=pygame.image.load("finish.jpg")
#remise en forme des images :
image1_resized=pygame.transform.scale(image1, (30,30))
image2_resized=pygame.transform.scale(image2, (40,40))
image3_resized=pygame.transform.scale(image3, (35,35))
image4_resized=pygame.transform.scale(image4, (1200*2/3,630*2/3))
pygame.mixer.music.load(song1)
#initialisation des scores des deux joueurs :
a=0
b=0
#nombre de fois à toucher le boutton bleu (la bière) avant de pouvoir gagner:
nb_carre_pour_gagner=10




#Initialiser les rectangles.
rectrouge=pygame.Rect(760,760,30,30)
rectbleu=pygame.Rect(20,20,30,30)
button=pygame.Rect(random.randint(10,790),random.randint(10,790),40,40)
pirate=pygame.Rect(ligne*7, ligne*2, 35,35)
                   

#vitesse de déplacement des rectangles (décapsuleurs)
speed=1 
running = True
timer_initial=time.time()
#lancement de la musique
pygame.mixer.music.play()
#boucle principale:
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    

    #réinitialisation des paramètres en cas d'appui sur la barre espace
    #après une victoire d'un des deux joueurs pour recommencer une partie
    if restart:
        a=0
        b=0
        nb_carre_pour_gagner=10
        rectrouge=pygame.Rect(760,760,30,30)
        rectbleu=pygame.Rect(20,20,30,30)
        button=pygame.Rect(random.randint(10,790),random.randint(10,790),40,40)
        pirate=pygame.Rect(ligne*7, ligne*2, 35,35)
        timer_initial=time.time()
        restart=False

    #Définition des appuis sur les touches de délpaement des joueurs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rectrouge.x -= speed
        if collide():
           rectrouge.x += speed
    if keys[pygame.K_RIGHT]:
        rectrouge.x += speed
        if collide():
           rectrouge.x -=speed
    if keys[pygame.K_UP]:
        rectrouge.y -= speed
        if collide():
           rectrouge.y +=speed
    if keys[pygame.K_DOWN]:
        rectrouge.y += speed
        if collide():
           rectrouge.y -=speed
    if keys[pygame.K_a]:
        rectbleu.x -= speed
        if collideblue():
           rectbleu.x +=speed
    if keys[pygame.K_d]:
        rectbleu.x += speed
        if collideblue():
           rectbleu.x -=speed
    if keys[pygame.K_w]:
        rectbleu.y -= speed
        if collideblue():
           rectbleu.y +=speed
    if keys[pygame.K_s]:
        rectbleu.y += speed
        if collideblue():
           rectbleu.y -=speed
    
    #actions des touches qui agissent sur la musique
    
    #arrêter toute musique
    if keys[pygame.K_0]:
        pygame.mixer.music.stop()
    #lancer musique 1
    if keys[pygame.K_1]:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(song1)
        pygame.mixer.music.play()
    #lancer musique 2
    if keys[pygame.K_2]:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(song2)
        pygame.mixer.music.play()
    #lancer musique 3
    if keys[pygame.K_3]:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(song3)
        pygame.mixer.music.play()
    
    #Définition d'un nouvel emplacement pour la bière lorsqu'un joueur l'a collisionnée
    while collidebutton():
        print("collision boutton bleu")
        button.x=random.randint(10,790)
        button.y=random.randint(10,790)

    
    
    if rectbleu.colliderect(button):
        test=True
        
        
        button.x=random.randint(10,790)
        button.y=random.randint(10,790)
                
        a+=1
    if rectrouge.colliderect(button):
        test=True
        
        
        button.x=random.randint(10,790)
        button.y=random.randint(10,790)
                
        b+=1    
        

    #trouver une nouvelle position pour la bière sans qu'elle colisionne un mur
    while collidebutton():
        print("collision boutton bleu")
        button.x=random.randint(10,790)
        button.y=random.randint(10,790)
    
    
      
                    
    #fait perdre un joueur si celui-ci collisionne la bouteille d'eau
    if rectrouge.colliderect(pirate) :
        #os.system('shutdown /s /t 1')
        a=nb_carre_pour_gagner+1
    if rectbleu.colliderect(pirate):
        #os.system('shutdown /s /t 1')
        b=nb_carre_pour_gagner+1
        
                    
    if collide():
        print("colision")
       
    if collideblue():
        print("colision")
    #préparation de la variable timer lors de la partie pour l'afficher par la suite
    if a<nb_carre_pour_gagner and b<nb_carre_pour_gagner :
        timer=time.time()-timer_initial
        timer=round(timer,1)
        timer=str(timer)
    #possibilité d'afficher les règles du jeu
    if keys[pygame.K_r]:
        screen.fill(blue)
        screen.blit(font_regles_titre.render("Règles du jeu",True, (250,0,0)),(40,40))
        screen.blit(font_regles.render("Le jeu est une course entre les deux joueurs,", True,(255,0,0)),(40,110))
        screen.blit(font_regles.render("chaque joueur dirige un décapsuleur grâce aux touches ", True,(255,0,0)),(40,160))
        screen.blit(font_regles.render("W+A+S+D ou aux touches des flèches vers le haut,", True,(255,0,0)),(40,210))
        screen.blit(font_regles.render("la droite, la gauche et le  bas.", True,(255,0,0)),(40,260))
        screen.blit(font_regles.render((f"Le but de chaque joueur est de ramasser {nb_carre_pour_gagner} fois la"), True,(255,0,0)),(40,360))
        screen.blit(font_regles.render("bouteille de bière avant l'autre joueur, ", True,(255,0,0)),(40,410))
        screen.blit(font_regles.render("mais de ne prendre que la bouteille de bière...", True,(255,0,0)),(40,460))
        screen.blit(font.render("...car l'eau de se décapsule pas.", True,(255,0,0)),(40,710))
        screen.blit(font_regles.render("Appuyez les touches 1 à 3 pour changer la musique",  True, (255,0,0)),(40,780))
        screen.blit(font_regles.render("et la touche 0 pour l'arrêter.",  True, (255,0,0)),(40,810))
        pygame.display.flip()
        
    else:
        #application de tout ce qui a été préparé:
        screen.fill((255, 255, 255))

        screen.blit(font.render(timer, True, (0,0,0)), (350,800))
        screen.blit(font.render((f"{a}/{nb_carre_pour_gagner} bières"),True, (0,0,0)),(0,800))
        screen.blit(font.render((f"{b}/{nb_carre_pour_gagner} bières"),True, (0,0,0)),(550,800))

        for rect in rect_List:
            pygame.draw.rect(screen, (0,0,0), rect)
        pygame.draw.rect(screen, (255, 0, 0), (rectrouge))
        screen.blit(image1_resized,rectrouge)
        pygame.draw.rect(screen, (0, 0, 255), (rectbleu))
        screen.blit(image1_resized,rectbleu)
        pygame.draw.rect(screen, (0, 255, 255), (button))
        pygame.draw.rect(screen,(0,50,50), (pirate))
        screen.blit(image3_resized,pirate)
        
        
        
        
        
        screen.blit(image2_resized,(button.x,button.y))
        
        
    if a>=nb_carre_pour_gagner:
    
    #conditions pour gagner:
    
        print("finish")
        screen.fill(yellow)
        screen.blit(image4_resized,(0,0))
        screen.blit(font.render((f"le joueur avec les lettres a gagné"), True, (0,255,0)),(10,200))
        screen.blit(font.render((f"barre espace pour recommencer"), True, (0,255,0)),(10,280))
        screen.blit(font.render((f" en {timer} secondes! Pressez sur la "), True, (0,255,0)), (10,240))
        pygame.display.flip()
        
        
        if keys[pygame.K_SPACE]:
            restart= True
            
        
    if b>=nb_carre_pour_gagner:
    
    #conditions pour gagner:
    
        print("finish")
        screen.fill(yellow)
        screen.blit(image4_resized, (0,0))
        screen.blit(font.render((f"le joueur avec les flèches a gagné "), True, (0,255,0)),(10,200))
        screen.blit(font.render((f"barre espace pour recommencer "), True, (0,255,0)),(10,280))
        screen.blit(font.render((f"en {timer} secondes! Pressez sur la"), True, (0,255,0)),(10,240))
        pygame.display.flip()
        if keys[pygame.K_SPACE]:
            restart= True
        
    pygame.display.flip()
    time.sleep(0.005) 
#fin du programme