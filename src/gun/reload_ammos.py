import pygame

class Reload:
    def __init__(self, reload_time):
        self.reload_time = reload_time
        self.is_reload = False
        self.reload_timer = 0  
    
    def reloadMag(self, delta):
        self.reload_timer += delta * 1000
        if self.reload_timer >= self.reload_time:
            self.reload_timer = 0
            self.ammos = self.ammos_max
            self.reloading = False
            
    def getTimeReload(self, delta):
        time_remaining = round((self.reload_time - self.reload_timer)/1000, 1)
        return time_remaining if self.reloading else 0