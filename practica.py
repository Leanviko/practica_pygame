import pygame, sys, random

pygame.init()




WEIGHT = 800
HEIGTH = 500

#* creamos la ventana
pantalla = pygame.display.set_mode((WEIGHT, HEIGTH))
#* reloj 
reloj = pygame.time.Clock() 
background = pygame.image.load("Images/Nebula.png").convert()
nave = pygame.image.load("Images/nave.png").convert_alpha()

#*propiedades del cuadrado
cord_x = 300
cord_y = 200
        #*velocidad del cuadrado
# velocidad_x = 3
# velocidad_y = 3

#mouse
pygame.mouse.set_visible(False) #Esconde el puntero en la pantalla
#bucle principal



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        
    ###-----INICIO LOGICA----###
    
    mouse_posicion = pygame.mouse.get_pos()
    cord_x = mouse_posicion[0]
    cord_y = mouse_posicion[1]
    ###-----fin LOGICA----###

    pantalla.blit(background, (0,0))
    pantalla.blit(nave,(cord_x,cord_y)) 
    
    ###-----INICIO ZONA DE DIBUJO----###
    
    

    

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