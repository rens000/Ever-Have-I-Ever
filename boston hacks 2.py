import pygame
from pygame.locals import *
import time


pygame.init()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
black = (0,0,0)
  
x = 750
y = 750
persons = []

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
    return int(num)

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
    persons.append(Person(num, 5))
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
    screen.fill(white)
    pygame.display.update()
    for i in range(num):
        
        name = get_names_question(player_number)
        list_of_names.append(name)
        player_number += 1
        
    return list_of_names



def display_prompt(name):
    text = font.render("It's your turn " + name + "!", True, blue, white) 
    textRect = text.get_rect()  
    textRect.center = (x // 2, y // 2.5)
    screen.fill(white) 
    screen.blit(text, textRect)
    pygame.display.update()
    
def get_question(name):
    display_prompt(name)
    prompt = ""
    check = True
    while check:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                screen.fill((250,250,250))
                display_prompt(name)
                if evt.key == K_BACKSPACE:
                    prompt = prompt[:-1]
                elif evt.key == K_RETURN:
                    check = False
                else:
                    prompt += evt.unicode
            elif evt.type == QUIT:
                return
        block = font.render("Ever have I ever... " + prompt, True, (blue))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()
    return prompt



def display_answers(prompt, name, names):
    text = font.render(name + "! Have you ever " + prompt + "?", True, blue, white) 
    textRect = text.get_rect()  
    textRect.center = (x // 2, y // 2.5)
    screen.fill(white)
    display_names()
    screen.blit(text, textRect)
    pygame.display.update()

def get_answers(prompt):
    answers = [0] * num
    for i in range(num):
        display_answers(prompt, names[i], names)
        check = True
        while check:
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    screen.fill((250,250,250))
                    display_answers(prompt, names[i], names)
                    if evt.key == K_t:
                        answers[i] = 1
                        check = False
                    elif evt.key == K_f:
                        answers[i] = 0
                        persons[i].points -= 1
                        check = False
                elif evt.type == QUIT:
                    return
            
    return answers



def print_name(person, x_name, y_name):
    font = pygame.font.Font('freesansbold.ttf', 18)
    text = font.render(person.name + ": " + str(person.points), True, black, white) 
    textRect = text.get_rect()  
    textRect.center = (x_name, y_name)
    screen.blit(text, textRect)
    pygame.display.update()


def display_names():
    screen.fill(white) 
    x_name = x/10
    y_name = y / 10
    for person in persons:
        print_name(person, x_name, y_name)
        x_name += x/len(persons) 

class Person:
    def __init__(self, name, points):
        self.name = name
        self.points = points


def display_answers(prompt, name):
    text = font.render(name + "! Have you ever " + prompt + "?", True, blue, white) 
    textRect = text.get_rect()  
    textRect.center = (x // 2, y // 2.5)
    screen.fill(white) 
    screen.blit(text, textRect)
    pygame.display.update()

def get_answers(prompt):
    answers = [0] * num
    for i in range(num):
        display_answers(prompt, names[i])
        check = True
        while check:
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    screen.fill((250,250,250))
                    display_answers(prompt, names[i])
                    if evt.key == K_t:
                        answers[i] = 1
                        check = False
                    elif evt.key == K_f:
                        answers[i] = 0
                        check = False
                elif evt.type == QUIT:
                    return
            
    return answers


### MAIN
num = get_num_players()
names = get_names()

for i in range(3):
    for name in names:
        prompt = get_question(name)
        answers = get_answers(prompt)
        print(answers)



