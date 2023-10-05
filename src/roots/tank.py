import pygame

class Tank:
    def __init__(self, x, y, hp):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.hp = hp
        self.hp_max = hp
    
    def update(self):
        ...
        
    def draw(self, screen):
        pygame.draw.rect(screen, 'WHITE', self.rect, 0, 10)
        pygame.draw.circle(screen, 'BLACK', self.rect.center, 8)
        
        end_posx_red = (self.rect.right - self.rect.left) * (self.hp/self.hp_max) + self.rect.left
        pygame.draw.line(screen, 'WHITE', (self.rect.left, self.rect.topleft[1] - 10), (self.rect.right, self.rect.topright[1] - 10), 3)
        pygame.draw.line(screen, 'RED', (self.rect.left, self.rect.topleft[1] - 10), (end_posx_red, self.rect.topright[1] - 10), 3)