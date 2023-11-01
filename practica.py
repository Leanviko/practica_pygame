import pygame, sys, random

pygame.init()




WEIGHT = 800
HEIGTH = 500

#* creamos la ventana
pantalla = pygame.display.set_mode((WEIGHT, HEIGTH))
#* reloj 
reloj = pygame.time.Clock() 

#*propiedades del cuadrado
cord_x = 300
cord_y = 200
        #*velocidad del cuadrado
velocidad_x = 3
velocidad_y = 3


#bucle principal

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        

    #* limites al movimiento
    if(cord_x > 720 or cord_x < 0):
        velocidad_x *= -1
    if(cord_y > 420 or cord_y < 0):
        velocidad_y *= -1

    cord_x += velocidad_x
    cord_y += velocidad_y

    
    pantalla.fill((150,255,100)) #* pinta la pantalla del color
    ###-----INICIO ZONA DE DIBUJO----###
    
    pygame.draw.rect(pantalla, (200,10,50), (cord_x,cord_y, 80, 80))

    

    ###-----FIN ZONA DE DIBUJO----###
    pygame.display.flip() #*actualiza la pantalla
    reloj.tick(60) #*fps


