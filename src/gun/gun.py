import pygame
from src.gun.magazine import Magazine
from src.gun.fire import Fire
from src.gun.reload_ammos import Reload
from pygame.locals import *

class Gun(Magazine, Fire, Reload):
    def __init__(self, name, ammos, speed, delay_fire, reloadTime, damage, color, size):
        Magazine.__init__(self, ammos, damage, color, size, speed)
        Fire.__init__(self, delay_fire)
        Reload.__init__(self, reloadTime)
        self.name = name
        
        
    def update(self, player_pos, mouse_pos, delta):
        if pygame.key.get_pressed()[K_r]:
            self.ammos = 0
        if self.ammos <= 0:
            self.reloading = True
            self.reloadMag(delta)
        else:
            self.fire(player_pos, mouse_pos, delta)
                
    

    
    def draw(self, screen, mouse_pos, player_pos):
        V_mouse = pygame.Vector2(mouse_pos[0], mouse_pos[1])
        V_player = pygame.Vector2(player_pos[0], player_pos[1])

        length = pygame.math.Vector2.magnitude(V_mouse-V_player)
        if length != 0:
            self.end_posx = ((mouse_pos[0] - player_pos[0]) * 30)/length + player_pos[0]
            self.end_posy = ((mouse_pos[1] - player_pos[1]) * 30)/length + player_pos[1]
        pygame.draw.line(screen, 'AQUA', player_pos, (self.end_posx, self.end_posy), 5)