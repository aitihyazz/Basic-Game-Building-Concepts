import pygame
pygame.init()
screen= pygame.display.set_mode((400,400))
screen.fill((225,225,0))
GREEN=(0,225,0)
pygame.draw.circle(screen,GREEN,(300,300),50)
pygame.draw.circle(screen,GREEN,(100,100),50,3)
pygame.display.update()
r=True
while r:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running =False
    pygame.display.flip()
