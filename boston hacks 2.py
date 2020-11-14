import pygame
from pygame.locals import *
import time


pygame.init()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
  
x = 750
y = 750

screen = pygame.display.set_mode((x, y)) 
pygame.display.set_caption('Ever Have I Ever') 
font = pygame.font.Font('freesansbold.ttf', 35)

def get_num_players():
    text = font.render('How many players do you have?', True, blue, white) 
    textRect = text.get_rect()  
    textRect.center = (x // 2, y // 2.5)

    screen.fill(white) 
    screen.blit(text, textRect)
    pygame.display.update()

    num = ''
    check = True
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.key == K_BACKSPACE:
                    num = num[:-1]
                elif evt.key == K_RETURN:
                    check = False
                else:
                    num += evt.unicode
            elif evt.type == QUIT:
                return
        #screen.fill((250,250,250))
        block = font.render(num, True, (blue))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()
    print(num)




get_num_players()



