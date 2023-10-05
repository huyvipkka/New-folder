import pygame
from src.characters.player import Player
from src.gun.gun import Gun

pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
FPS = 60
delta = 1/FPS
running = True

dict_gun = {
    pygame.K_1 : Gun('Gatling gun', ammos=100, speed=400, delay_fire=50, reloadTime=5000, damage=5, color='white', size=10),  
    pygame.K_2 : Gun('Pistol', ammos=10, speed=600, delay_fire=400, reloadTime=1500, damage=40, color='yellow', size=15),
    pygame.K_3 : Gun('Cannon', ammos=6, speed=400, delay_fire=1000, reloadTime=3000, damage=100, color='red', size=25)
}
player = Player(400, 500, 10, 200, dict_gun)

while running:
    screen.fill("black")
    
    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player.update(key, mouse_pos, 900, 600, delta)

    player.draw(screen, mouse_pos)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()