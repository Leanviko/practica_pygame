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
        self.vidas = 5

    
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
            laser_nave.play()
        if pygame.mouse.get_pressed()[0] == False:
            self.disparo = False
        
        
    def update(self):
        if self.mover_derecha and self.rect.right < WIDHT:
            self.rect.x += 5
        if self.mover_izquierda and self.rect.left > 0:
            self.rect.x -= 5
        if self.mover_arriba and self.rect.top > 0:
            self.rect.y -= 5
        if self.mover_abajo and self.rect.bottom < HEIGTH:
            self.rect.y += 5
        
        if self.vidas <= 0:
            self.vidas = 0

        

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

        enemigos_colision_nave = pygame.sprite.spritecollide(nave, enemigos_lista, True)
        if enemigos_colision_nave:
            nave.vidas -= 1

        if self.rect.right > 550 or self.rect.left < 50:
            self.velocidad_x *= -1
        elif self.rect.top > 800:
            self.rect.x = random.randrange(100,500)
            self.rect.bottom = -1*random.randrange(10,700)

    

class Enemigo_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/meteorito.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        
        self.rect.y += 2
        enemigo_2_colision_lista = pygame.sprite.spritecollide(nave, enemigo_2_lista, True)
        if enemigo_2_colision_lista:
            nave.vidas -= 1

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

def mostrar_puntaje(pantalla, fuente, texto, color, dimension, x, y): 
    texto_puntaje = pygame.font.SysFont(fuente, dimension,True)
    superficie = texto_puntaje.render(texto,True,color,None)
    rectangulo = superficie.get_rect()
    rectangulo.right = x
    rectangulo.top = y
    pantalla.blit(superficie,rectangulo)

def mostrar_vida(pantalla, fuente, texto, color, dimension, x, y): 
    texto_puntaje = pygame.font.SysFont(fuente, dimension,True)
    superficie = texto_puntaje.render(texto,True,color,None)
    rectangulo = superficie.get_rect()
    rectangulo.left = x
    rectangulo.top = y
    pantalla.blit(superficie,rectangulo)

def Escribir_texto(pantalla, fuente, texto, color, dimension, x, y): 
    texto_puntaje = pygame.font.SysFont(fuente, dimension,True)
    superficie = texto_puntaje.render(texto,True,color,None)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x,y)
    pantalla.blit(superficie,rectangulo)

class Boton(pygame.sprite.Sprite):
    def __init__(self,pantalla,imagen,x,y):
        self.image= imagen
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        pantalla.blit(self.image,self.rect)


WIDHT = 600
HEIGTH = 800
inicio = True
corriendo = False
final = False


pygame.init()


pygame.mixer.music.load('Sounds/Thunder Force IV OST 06 - Evil Destroyer.mp3')
laser_nave = pygame.mixer.Sound('Sounds/disparo_nave.wav')
explosion_enemigo = pygame.mixer.Sound('Sounds/explosion_enemigo.wav')
laser_nave.set_volume(0.2) 
explosion_enemigo.set_volume(0.4) 
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

pantalla = pygame.display.set_mode((WIDHT, HEIGTH)) 
reloj = pygame.time.Clock() 
background = pygame.image.load("Images/Nebula.png").convert()

puntaje = 0


#*grupos de sprites
enemigo_2_lista = pygame.sprite.Group()
laser_lista = pygame.sprite.Group()
laser_enemigo_lista = pygame.sprite.Group()
enemigos_lista = pygame.sprite.Group()
todos_sprites_lista = pygame.sprite.Group()

for i in range(10):
        enemigo_2 = Enemigo_2()
        enemigo_2.rect.x = random.randrange(WIDHT)
        enemigo_2.rect.y = random.randrange(HEIGTH)
        enemigo_2_lista.add(enemigo_2)
        todos_sprites_lista.add(enemigo_2)
for i in range(3): 
        enemigo = Enemigo()
        enemigo.rect.bottom = -1*random.randrange(10,700)
        enemigos_lista.add(enemigo)
        todos_sprites_lista.add(enemigo)


nave = Nave()
todos_sprites_lista.add(nave)
game_over = False
#bucle principal-------------------------------------------------------

while inicio:
    boton_inicio = pygame.image.load("Images/inicio.png").convert_alpha()
    boton_salir = pygame.image.load("Images/salir.png").convert_alpha()
    reloj.tick(23)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
    
    pantalla.fill((0,0,0))
    boton_inicio = Boton(pantalla,boton_inicio,WIDHT/2,500)
    boton_salir = Boton(pantalla,boton_salir,WIDHT/2,600)
    Escribir_texto(pantalla,'Arial', "Inicio", (255,255,255), 50 ,WIDHT/2,HEIGTH/2)
    #Escribir_texto(pantalla,'Arial', "presione click", (255,255,255), 20 ,WIDHT/2,500)

    if boton_inicio.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        inicio = False
        corriendo = True
    if boton_salir.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        sys.exit()
    
    pygame.display.update()
        


while corriendo:


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
            enemigo_2_colision_lista = pygame.sprite.spritecollide(laser, enemigo_2_lista, True)
            enemigo_colision_lista = pygame.sprite.spritecollide(laser, enemigos_lista, True)
            

            if enemigo_colision_lista:
                puntaje += 10
            if enemigo_2_colision_lista:
                puntaje += 1
            
            for enemigo_2 in enemigo_2_colision_lista:
                todos_sprites_lista.remove(laser)
                laser_lista.remove(laser)
                explosion_enemigo.play()

                enemigo_2 = Enemigo_2()
                enemigo_2.rect.x = random.randrange(WIDHT)
                enemigo_2.rect.bottom = -1*random.randrange(100,500)
                enemigo_2_lista.add(enemigo_2)
                todos_sprites_lista.add(enemigo_2)

            for enemigo in enemigo_colision_lista:
                todos_sprites_lista.remove(laser)
                laser_lista.remove(laser)
                explosion_enemigo.play()

                enemigo = Enemigo()
                enemigo.rect.bottom = -1*random.randrange(10,700)
                enemigos_lista.add(enemigo)
                todos_sprites_lista.add(enemigo)

    for laser_enemigo in laser_enemigo_lista:
        enemigo_laser_lista = pygame.sprite.spritecollide(nave, laser_enemigo_lista, True)

        if enemigo_laser_lista:
            nave.vidas -= 1

    if nave.vidas == 0:
        corriendo = False
        final = True
        pygame.mixer.music.stop()

    todos_sprites_lista.update()
    ###-----fin LOGICA----###
    pantalla.blit(background, (0,0))
    ###-----INICIO ZONA DE DIBUJO----###
    todos_sprites_lista.draw(pantalla)
    nave.disparar()
    enemigo.disparar()

    mostrar_puntaje(pantalla,'Arial',f'puntaje: {str(puntaje).zfill(4)}',(255,255,255),30,WIDHT-70, 50)
    mostrar_vida(pantalla,'Arial',str(f'Vidas: {nave.vidas}'),(255,255,255),30,50, 50)

    while final:
        reloj.tick(23)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
    
        pantalla.fill((0,0,0))
        Escribir_texto(pantalla,'Arial', "Estas muerto", (255,100,100), 50 ,WIDHT/2,HEIGTH/2)
        Escribir_texto(pantalla,'Arial', f"puntaje: {puntaje}", (255,255,255), 20 ,WIDHT/2,500)

    
        pygame.display.update()
    
    

    ###-----FIN ZONA DE DIBUJO----###
    pygame.display.flip() #*actualiza la pantalla
    reloj.tick(60) #*fps





