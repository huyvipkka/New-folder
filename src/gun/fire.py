import pygame

class Fire:
    def __init__(self, delay_fire):
        self.delay_fire = delay_fire
        self.shoot_timer = 0
        
    def fire(self, player_pos, mouse_pos, delta):
        self.shoot_timer += delta * 1000
        if pygame.mouse.get_pressed()[0]:
            if self.shoot_timer >= self.delay_fire:
                self.shoot_timer = 0  # Update the shot timer
                self.magazine[self.ammos-1].reset(player_pos, mouse_pos)
                self.magazine[self.ammos-1].active = True
                self.ammos -= 1