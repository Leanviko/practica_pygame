import math
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

        self.disparo= False

    
    def disparar(self):
        posicion_mira = pygame.mouse.get_pos()
        dist_x = posicion_mira[0] - self.rect.midtop[0]
        dist_y = -(posicion_mira[1] - self.rect.midtop[1])
        self.angulo = math.degrees(math.atan2(dist_x,dist_y))

        if pygame.mouse.get_pressed()[0] and self.disparo == False:
            self.disparo = True
            laser_ob = Laser(self.rect.midtop[0],self.rect.midtop[1],self.angulo)
            laser_lista.add(laser_ob)
            todos_sprites_lista.add(laser_ob)
        if pygame.mouse.get_pressed()[0] == False:
            self.disparo = False
        
        
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
        self.ritmo_disparo = 1000
        self.ultimo_disparo = pygame.time.get_ticks()
    #----------------------------------------------------------------experimental
    def disparar(self):
        posicion_nave = nave.rect.center
        dist_x = posicion_nave[0] - self.rect.midbottom[0]
        dist_y = -(posicion_nave[1] - self.rect.midbottom[1])
        self.angulo = math.degrees(math.atan2(dist_x,dist_y))

        tiempo = pygame.time.get_ticks()
        
        if  (tiempo - self.ultimo_disparo > self.ritmo_disparo) and self.rect.top < nave.rect.top:
            laser_ob = Laser(self.rect.midbottom[0],self.rect.midbottom[1],self.angulo)
            laser_enemigo_lista.add(laser_ob)
            todos_sprites_lista.add(laser_ob)
            self.ultimo_disparo = tiempo
        
    #----------------------------------------------------------------

    def update(self):
        self.rect.y += 2
        self.rect.x += self.velocidad_x
        if self.rect.right > 550 or self.rect.left < 50:
            self.velocidad_x *= -1
        elif self.rect.top > 800:
            self.rect.x = random.randrange(100,500)
            self.rect.bottom = -1*random.randrange(10,700)

    

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
    def __init__(self,x,y,angulo):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/laser.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angulo = math.radians(angulo)#*convierte angulo a radianes
        self.velocidad_laser = 11
        self.dx = math.sin(self.angulo)*self.velocidad_laser
        self.dy = -(math.cos(self.angulo)*self.velocidad_laser)
        
    def update(self):
        if self.rect.right <0  or self.rect.top < 0 or self.rect.bottom >HEIGTH or self.rect.left > WIDHT:
            self.kill()

        #movimiento
        self.rect.x += self.dx
        self.rect.y += self.dy

        
WIDHT = 600
HEIGTH = 800
#*puntaje


            


pygame.init()




pantalla = pygame.display.set_mode((WIDHT, HEIGTH)) 
reloj = pygame.time.Clock() 
background = pygame.image.load("Images/Nebula.png").convert()

puntaje = 0
def mostrar_texto(pantalla, fuente, texto, color, dimension, x, y): 
    texto_puntaje = pygame.font.SysFont(fuente, dimension,True)
    superficie = texto_puntaje.render(texto,True,color,None)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x,y)
    pantalla.blit(superficie,rectangulo)



#*grupos de sprites
meteoro_lista = pygame.sprite.Group()
laser_lista = pygame.sprite.Group()
laser_enemigo_lista = pygame.sprite.Group()
enemigos_lista = pygame.sprite.Group()
todos_sprites_lista = pygame.sprite.Group()

for i in range(10):
        meteoro = Meteoro()
        meteoro.rect.x = random.randrange(WIDHT)
        meteoro.rect.y = random.randrange(HEIGTH)
        meteoro_lista.add(meteoro)
        todos_sprites_lista.add(meteoro)
for i in range(3): 
        enemigo = Enemigo()
        enemigo.rect.bottom = -1*random.randrange(10,700)
        enemigos_lista.add(enemigo)
        todos_sprites_lista.add(enemigo)


nave = Nave()
todos_sprites_lista.add(nave)

#bucle principal-------------------------------------------------------
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a: 
                nave.mover_izquierda = True
            if evento.key == pygame.K_d:
                nave.mover_derecha = True
            if evento.key == pygame.K_w:
                nave.mover_arriba = True
            if evento.key == pygame.K_s:
                nave.mover_abajo = True
            

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a: 
                nave.mover_izquierda = False
            if evento.key == pygame.K_d:
                nave.mover_derecha = False
            if evento.key == pygame.K_w:
                nave.mover_arriba = False
            if evento.key == pygame.K_s:
                nave.mover_abajo = False
            
        
        
    ###-----INICIO LOGICA----###
    for laser in laser_lista:
            meteoro_colision_lista = pygame.sprite.spritecollide(laser, meteoro_lista, True)

            enemigo_colision_lista = pygame.sprite.spritecollide(laser, enemigos_lista, True)

            if enemigo_colision_lista:
                puntaje += 1
            
            
            for meteoro in meteoro_colision_lista:
                todos_sprites_lista.remove(laser)
                laser_lista.remove(laser)

                meteoro = Meteoro()
                meteoro.rect.x = random.randrange(WIDHT)
                meteoro.rect.bottom = -1*random.randrange(100,500)
                meteoro_lista.add(meteoro)
                todos_sprites_lista.add(meteoro)

            for enemigo in enemigo_colision_lista:
                todos_sprites_lista.remove(laser)
                laser_lista.remove(laser)
                

                enemigo = Enemigo()
                enemigo.rect.bottom = -1*random.randrange(10,700)
                enemigos_lista.add(enemigo)
                todos_sprites_lista.add(enemigo)
    
    todos_sprites_lista.update()
    
    ###-----fin LOGICA----###
    pantalla.blit(background, (0,0))
    ###-----INICIO ZONA DE DIBUJO----###
    todos_sprites_lista.draw(pantalla)
    nave.disparar()
    enemigo.disparar()

    mostrar_texto(pantalla,'Arial',str(puntaje),(255,255,255),48,550, 50)
    
    

    ###-----FIN ZONA DE DIBUJO----###
    pygame.display.flip() #*actualiza la pantalla
    reloj.tick(60) #*fps





