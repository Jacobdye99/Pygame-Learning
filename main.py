import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption("Bugged")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Assets/Fonts/ka1.ttf", 50)

sky_surface = pygame.image.load('Assets/Sky2.png').convert_alpha()
ground_surface = pygame.image.load("Assets/Ground2.png").convert_alpha()
text_surface = test_font.render("Jacob's Game", False, "Black")

skull_surface = pygame.image.load("Assets/Characters/SkullBoy(2).png").convert_alpha()
skull_rect = skull_surface.get_rect(midbottom = (1000, 730))


player_surf = pygame.image.load("Assets/Characters/Idle.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (50, 738))

ground = pygame.transform.scale(ground_surface, (1650, 250))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(sky_surface, (0,0))
    
    
    skull_rect.left -= 4
    if skull_rect.right < 0: skull_rect.left = 1600
    screen.blit(skull_surface, skull_rect)
    screen.blit(player_surf, player_rect)
    
    
    screen.blit(ground, (-10,570))
    screen.blit(text_surface, (800,400))
    
    print(player_rect.colliderect(skull_rect))
    
    pygame.display.update()
    clock.tick(60)
    