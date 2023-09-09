import pygame

class Reload:
    def __init__(self, reload_time):
        self.reload_time = reload_time
        self.is_reload = False
        self.shoot_timer = 0  
    
    def reloadMag(self, current_time):
        if current_time - self.shoot_timer >= self.reloadTime:
            self.shoot_timer = current_time
            self.ammos = self.ammos_max
            self.reloading = False
            
    def getTimeReload(self, current_time):
        time_remaining = round((self.reloadTime - (current_time - self.shoot_timer))/1000, 1)
        return time_remaining if self.reloading else 0