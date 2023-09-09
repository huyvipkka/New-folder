import pygame
from classes.roots.move import PlayerMove
from classes.roots.tank import Tank
from classes.gun.gun import Gun

class Player(PlayerMove, Tank):
    def __init__(self, x, y, hp, speed, dict_gun):
        PlayerMove.__init__(self, speed)
        Tank.__init__(self, x, y, hp)
        self.dict_gun = dict_gun
        self.gun = dict_gun[pygame.K_1]
            
    def update(self, key, mouse_pos, current_time, scr_width, scr_height):
        self.move(key, scr_height, scr_width)
        self.gun.update(self.rect.center ,mouse_pos, current_time)
        for bul in self.gun.magazine:
            bul.update(scr_width, scr_height)
    
    def draw(self, screen, mouse_pos):
        pygame.draw.rect(screen, 'WHITE', self.rect, 0, 10)
        pygame.draw.circle(screen, 'BLACK', self.rect.center, 8)
        
        end_posx_red = (self.rect.right - self.rect.left) * (self.hp/self.hp_max) + self.rect.left
        pygame.draw.line(screen, 'WHITE', (self.rect.left, self.rect.topleft[1] - 10), (self.rect.right, self.rect.topright[1] - 10), 3)
        pygame.draw.line(screen, 'RED', (self.rect.left, self.rect.topleft[1] - 10), (end_posx_red, self.rect.topright[1] - 10), 3)
        self.gun.draw(screen, mouse_pos, self.rect.center)
        for bul in self.gun.magazine:
            bul.draw(screen)