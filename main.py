import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Bugged")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Assets/Fonts/ka1.ttf", 50)

sky_surface = pygame.image.load('Assets/Sky2.png')
ground_surface = pygame.image.load("Assets/Ground2.png")
text_surface = test_font.render("Jacob's Game", False, "Black")

skull_surface = pygame.image.load("Assets/Characters/SkullBoy(2).png")
skull_x_position = 1000

ground = pygame.transform.scale(ground_surface, (1650, 250))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(sky_surface, (0,0))
    skull_x_position -= 4
    if skull_x_position < -200: skull_x_position = 1650
    screen.blit(skull_surface, (skull_x_position,420))
    screen.blit(ground, (-10,570))
    screen.blit(text_surface, (800,400))
    
    pygame.display.update()
    clock.tick(60)
    