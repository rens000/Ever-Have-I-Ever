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

def display_question():
    text = font.render('How many players do you have?', True, blue, white) 
    textRect = text.get_rect()  
    textRect.center = (x // 2, y // 2.5)
    screen.fill(white) 
    screen.blit(text, textRect)
    pygame.display.update()
    

def get_num_players():
    display_question()
    num = ''
    check = True
    while check:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                screen.fill((250,250,250))
                display_question()
                if evt.key == K_BACKSPACE:
                    num = num[:-1]
                elif evt.key == K_RETURN:
                    check = False
                else:
                    num += evt.unicode
            elif evt.type == QUIT:
                return
        block = font.render(num, True, (blue))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()
    return num



    text = font.render('How many players do you have?', True, blue, white) 
    textRect = text.get_rect()  
    textRect.center = (x // 2, y // 2.5)
    screen.fill(white) 
    screen.blit(text, textRect)
    pygame.display.update()
    


def display_name_question(player_number):
    text = font.render('Player ' + str(player_number) + ': What is your name?', True, blue, white)
    textRect = text.get_rect()  
    textRect.center = (x // 2, y // 2.5)
    screen.fill(white) 
    screen.blit(text, textRect)
    pygame.display.update()


def get_names_question(player_number):
    display_name_question(player_number)
    num = ''
    check = True
    while check:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                screen.fill((250,250,250))
                display_name_question(player_number)
                if evt.key == K_BACKSPACE:
                    num = num[:-1]
                elif evt.key == K_RETURN:
                    check = False
                else:
                    num += evt.unicode
            elif evt.type == QUIT:
                return
        block = font.render(num, True, (blue))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()
    return num

    text = font.render("What is your name?", True, blue, white) 
    textRect = text.get_rect()  
    textRect.center = (x // 2, y // 2.5)
    screen.fill(white) 
    screen.blit(text, textRect)
    pygame.display.update()

    
def get_names():
    player_number = 1
    list_of_names= []
    num_players = int(get_num_players())
    screen.fill(white)
    pygame.display.update()
    for i in range(num_players):
        
        name = get_names_question(player_number)
        list_of_names.append(name)
        player_number += 1
        
    return list_of_names
        
def names_display():
    screen.fill(white)
    pygame.display.update()
    names = get_names()
    
        


print(get_names())
names_display()
    
    



