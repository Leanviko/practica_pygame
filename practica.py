import pygame, sys, random

class Meteoro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/meteorito.png").convert_alpha()
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/nave.png").convert_alpha()
        self.rect = self.image.get_rect()

pygame.init()

WEIGHT = 800
HEIGTH = 500

#* creamos la ventana
pantalla = pygame.display.set_mode((WEIGHT, HEIGTH))
#* reloj 
reloj = pygame.time.Clock() 
background = pygame.image.load("Images/Nebula.png").convert()

#*puntaje
puntaje = 0

#*grupos de sprites
meteoro_lista = pygame.sprite.Group()
todos_sprites_lista = pygame.sprite.Group()

#*creo meteoros
for i in range(12):
    meteoro = Meteoro()
    meteoro.rect.x = random.randrange(WEIGHT)
    meteoro.rect.y = random.randrange(HEIGTH)



    meteoro_lista.add(meteoro)
    todos_sprites_lista.add(meteoro)
    
#* nave como variable
nave = Player()
todos_sprites_lista.add(nave)

#mouse
pygame.mouse.set_visible(False) #Esconde el puntero en la pantalla
#bucle principal



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        
    ###-----INICIO LOGICA----###
    
    mouse_posicion = pygame.mouse.get_pos()
    nave.rect.x = mouse_posicion[0]
    nave.rect.y = mouse_posicion[1]

                #*colision con los meteoros
    meteoro_colision_lista = pygame.sprite.spritecollide(nave, meteoro_lista, True)

    for meteoro in meteoro_colision_lista:
        puntaje += 1
        print(puntaje)

    ###-----fin LOGICA----###
    pantalla.blit(background, (0,0))
    ###-----INICIO ZONA DE DIBUJO----###

    todos_sprites_lista.draw(pantalla)
    

    

    ###-----FIN ZONA DE DIBUJO----###
    pygame.display.flip() #*actualiza la pantalla
    reloj.tick(60) #*fps


#* limites al movimiento
    # if(cord_x > 720 or cord_x < 0):
    #     velocidad_x *= -1
    # if(cord_y > 420 or cord_y < 0):
    #     velocidad_y *= -1

    # cord_x += velocidad_x
    # cord_y += velocidad_y

#* pinta la pantalla del color
    #pantalla.fill((150,255,100)) 

#pygame.draw.rect(pantalla, (200,10,50), (cord_x,cord_y, 80, 80))

#*velocidad del cuadrado
# velocidad_x = 3
# velocidad_y = 3