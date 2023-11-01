import pygame, sys, random

class Meteoro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/meteorito.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        
        self.rect.y += 2
        if self.rect.top > 800:
            self.rect.bottom = -10
            self.rect.x = random.randrange(WIDHT)

        


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/nave.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = WIDHT/2
        self.rect.bottom = HEIGTH - 30
    
    def update(self):
        # mouse_posicion = pygame.mouse.get_pos()
        self.rect.x += velocidad_x
        self.rect.y += velocidad_y


pygame.init()

WIDHT = 600
HEIGTH = 800

#* creamos la ventana
pantalla = pygame.display.set_mode((WIDHT, HEIGTH))
#* reloj 
reloj = pygame.time.Clock() 
background = pygame.image.load("Images/Nebula.png").convert()

#*puntaje
puntaje = 0

#*grupos de sprites
meteoro_lista = pygame.sprite.Group()
todos_sprites_lista = pygame.sprite.Group()

for i in range(11):
    meteoro = Meteoro()
    meteoro.rect.x = random.randrange(WIDHT)
    meteoro.rect.y = random.randrange(HEIGTH)

    meteoro_lista.add(meteoro)
    todos_sprites_lista.add(meteoro)

#* nave como variable
nave = Player()
todos_sprites_lista.add(nave)

velocidad_x = 0
velocidad_y = 0

#mouse
pygame.mouse.set_visible(False) #Esconde el puntero en la pantalla

#bucle principal-------------------------------------------------------
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        print(evento)
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            velocidad_x = -2.5
        if keys[pygame.K_RIGHT]:
            velocidad_x = 2.5
        if keys[pygame.K_UP]:
            velocidad_y -= 2.5
        if keys[pygame.K_DOWN]:
            velocidad_y += 2.5
        if keys[pygame.K_LCTRL]:
            
                velocidad_x = 0
                velocidad_y = 0

        # if evento.type == pygame.KEYUP:
        #     if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
        #         velocidad_x = 0
        #     if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
        #         velocidad_y = 0
        
    ###-----INICIO LOGICA----###
    
    todos_sprites_lista.update()

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

    # 

#* pinta la pantalla del color
    #pantalla.fill((150,255,100)) 

#pygame.draw.rect(pantalla, (200,10,50), (cord_x,cord_y, 80, 80))

#*velocidad del cuadrado
# velocidad_x = 3
# velocidad_y = 3