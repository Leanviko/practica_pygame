import pygame, sys, random

pygame.init()



HEIGTH = 800
WEIGHT = 500

#* creamos la ventana
pantalla = pygame.display.set_mode((WEIGHT, HEIGTH))

#bucle principal

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    
    pantalla.fill((150,255,100)) #* pinta la pantalla del color
    ###-----INICIO ZONA DE DIBUJO----###
    pygame.draw.line(pantalla, (0,200,0),(10,100),(100,100),5)

    ###-----FIN ZONA DE DIBUJO----###
    pygame.display.flip() #*actualiza la pantalla


