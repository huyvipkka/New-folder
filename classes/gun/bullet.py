import pygame

class Bullet:
    def __init__(self, damage, color, size, speed):
        self.size = size
        self.image = pygame.Surface((size, size)) 
        self.rect = self.image.get_rect()  
        self.speed = speed
        self.active = False
        self.damage = damage
        self.color = color
        self.direction = pygame.Vector2(0, 0)
        
    def update(self, scr_width, scr_height):
        if self.active:
            if self.direction.length() > 0:
                self.direction.normalize_ip()
                self.rect.x += self.direction.x * self.speed
                self.rect.y += self.direction.y * self.speed
            
            if self.rect.x < 0 or self.rect.x > scr_width or self.rect.y < 0 or self.rect.y > scr_height:
                self.active = False
                
    def reset(self, player_pos, mouse_pos):
        self.rect.center = player_pos
        self.direction =  pygame.Vector2(mouse_pos) - pygame.Vector2(self.rect.center)
        
    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color, self.rect, 0, self.size//3)
    
    def inflictDmg(self):
        return self.damage if self.active else 0