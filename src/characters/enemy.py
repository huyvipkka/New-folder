import pygame
from src.roots.tank import Tank
import random

class Enemy(Tank):
    def __init__(self, hp, speed, scr_width, scr_height):
        x = random.randint(-100, 0) if random.getrandbits(1) else random.randint(scr_width, scr_width+100)
        y = random.randint(-100, 0) if random.getrandbits(1) else random.randint(scr_height, scr_height+100)
        Tank.__init__(self, x, y, hp)
        