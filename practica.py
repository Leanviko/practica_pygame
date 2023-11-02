import pygame, sys, random

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/nave.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = WIDHT/2
        self.rect.bottom = HEIGTH - 30
        self.mover_derecha = False
        self.mover_izquierda = False
        self.mover_arriba = False
        self.mover_abajo = False
        
    def update(self):
        
        if self.mover_derecha and self.rect.right < WIDHT:
            self.rect.x += 3
        if self.mover_izquierda and self.rect.left > 0:
            self.rect.x -= 3
        if self.mover_arriba and self.rect.top > 0:
            self.rect.y -= 3
        if self.mover_abajo and self.rect.bottom < HEIGTH:
            self.rect.y += 3

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/enemigo.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randrange(100,500)
        self.rect.bottom = -10
        
        self.velocidad_x = 4

    def update(self):
        self.rect.y += 2
        self.rect.x += self.velocidad_x
        if self.rect.right > 550 or self.rect.left < 50:
            self.velocidad_x *= -1
        elif self.rect.top > 800:
            self.rect.x = random.randrange(100,500)
            self.rect.bottom = -10

    

class Meteoro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/meteorito.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        
        self.rect.y += 2
        meteoro_colision_lista = pygame.sprite.spritecollide(nave, meteoro_lista, True)

        if self.rect.top > 800:
            self.rect.bottom = -10
            self.rect.x = random.randrange(WIDHT)



class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/laser.png").convert_alpha()
        self.rect = self.image.get_rect()

        
    def update(self):
        self.rect.y -= 11
        for laser in laser_lista:
            meteoro_colision_lista = pygame.sprite.spritecollide(laser, meteoro_lista, True)
            for meteoro in meteoro_colision_lista:
                todos_sprites_lista.remove(laser)
                laser_lista.remove(laser)
        if laser.rect.bottom < -10:
            todos_sprites_lista.remove(laser)
            laser_lista.remove(laser)
        
            


pygame.init()

WIDHT = 600
HEIGTH = 800

pantalla = pygame.display.set_mode((WIDHT, HEIGTH)) 
reloj = pygame.time.Clock() 
background = pygame.image.load("Images/Nebula.png").convert()

#*puntaje
puntaje = 0

#*grupos de sprites
meteoro_lista = pygame.sprite.Group()
laser_lista = pygame.sprite.Group()
enemigos_lista = pygame.sprite.Group()
todos_sprites_lista = pygame.sprite.Group()

for i in range(10):
        meteoro = Meteoro()
        meteoro.rect.x = random.randrange(WIDHT)
        meteoro.rect.y = random.randrange(HEIGTH)
        meteoro_lista.add(meteoro)
        todos_sprites_lista.add(meteoro)

enemigo = Enemigo()
enemigos_lista.add(enemigo)
todos_sprites_lista.add(enemigo)


#* nave como variable
nave = Nave()
todos_sprites_lista.add(nave)
laser = Laser()


#mouse
pygame.mouse.set_visible(False) #Esconde el puntero en la pantalla

#bucle principal-------------------------------------------------------
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT: 
                nave.mover_izquierda = True
            if evento.key == pygame.K_RIGHT:
                nave.mover_derecha = True
            if evento.key == pygame.K_UP:
                nave.mover_arriba = True
            if evento.key == pygame.K_DOWN:
                nave.mover_abajo = True
            if evento.key == pygame.K_SPACE:
                laser = Laser()
                laser.rect.center = nave.rect.center
                laser.rect.bottom = nave.rect.top
                laser_lista.add(laser)
                todos_sprites_lista.add(laser)

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT: 
                nave.mover_izquierda = False
            if evento.key == pygame.K_RIGHT:
                nave.mover_derecha = False
            if evento.key == pygame.K_UP:
                nave.mover_arriba = False
            if evento.key == pygame.K_DOWN:
                nave.mover_abajo = False
            
        
        
    ###-----INICIO LOGICA----###
    
    
    todos_sprites_lista.update()
    ###-----fin LOGICA----###
    pantalla.blit(background, (0,0))
    ###-----INICIO ZONA DE DIBUJO----###

    todos_sprites_lista.draw(pantalla)
    
    

    ###-----FIN ZONA DE DIBUJO----###
    pygame.display.flip() #*actualiza la pantalla
    reloj.tick(60) #*fps





