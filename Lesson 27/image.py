# pygame window 
import pygame
pygame.init()

window = pygame.display.set_mode((300,400))
window.fill("cyan")
bg_surf = pygame.transform.scale(pygame.image.load("background.png").convert(),(400,400))
next_surf = pygame.transform.scale(pygame.image.load("penguin.png").convert(),(400,400))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        window.blit(next_surf,(200,200))
        window.blit(bg_surf,(0,0))
    pygame.display.flip()

