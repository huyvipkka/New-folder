import pygame
from pygame.locals import *

class PlayerMove:
    def __init__(self, speed):
        self.speed = speed
                
    def move(self, key, SCREEN_WIDTH, SCREEN_HEIGHT):
        direction = pygame.math.Vector2(0, 0)
        if key[K_UP] or key[K_w]:
            direction.y -= 1
        if key[K_DOWN] or key[K_s]:
            direction.y += 1
        if key[K_LEFT] or key[K_a]:
            direction.x -= 1
        if key[K_RIGHT] or key[K_d]:
            direction.x += 1
        
        if direction.length() > 0:
            direction.normalize_ip()
        self.rect.centerx += direction.x * self.speed
        self.rect.centery += direction.y * self.speed
        self.not_out_scr(SCREEN_HEIGHT, SCREEN_WIDTH)
        
        
    def not_out_scr(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.left <= 0:
            self.rect.left = 0