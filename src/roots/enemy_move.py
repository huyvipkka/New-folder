import pygame

class EnemyMove:
    def __init__(self, speed):
        self.speed = speed
        
    def move(self, player_pos, delta):
        V_player = pygame.Vector2(player_pos[0], player_pos[1])
        V_self = pygame.Vector2(self.rect.center)
        direction = pygame.Vector2.normalize_ip(V_player - V_self)
        self.rect.x += direction[0] * self.speed * delta
        self.rect.y += direction[1] * self.speed * delta