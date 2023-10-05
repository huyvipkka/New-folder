import pygame
from src.gun.bullet import Bullet

class Magazine:
    def __init__(self, ammos, damage, color, size, speed):
        self.magazine = []
        self.ammos = ammos
        self.ammos_max = ammos
        for _ in range(self.ammos_max):
            bul = Bullet(damage, color, size, speed)
            self.magazine.append(bul)