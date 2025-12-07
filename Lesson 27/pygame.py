# pygame window 
import pygame
pygame.init()

window = pygame.display.set_mode((300,400))
window.fill("cyan")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()

