import pygame.font

class TablaPuntajes:
    def __init__(self, o_juego):
        self.pantalla = o_juego.pantalla
        self.pantalla_rect = self.pantalla.get_rect()
        self.juego = o_juego
        self.estadisticas = o_juego.estadisticas
        self.colorTexto = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

    def puntaje(self):
        self.puntaje_str = str(self.juego.puntaje)
        self.puntaje_imagen = self.font.render(self.puntaje_str,self.colorTexto,None)

        self.puntaje_rect = self.puntaje_imagen.get_rect()
        self.puntaje_rect.right = self.pantalla_rect.right - 20
        self.puntaje_rect.top = 20
    
    def despliege_puntaje(self):
        self.screen.blit(self.puntaje_imagen, self.puntaje_rect)