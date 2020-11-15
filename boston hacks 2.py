import pygame
from pygame.locals import *
import time


true = ["yeah", "yes", "y", "true", "t"]
false = ["no", "n", "nope", "false", "f", "never"]

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
    persons.append(Person(num, 2))
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
    display_names()
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


def get_a(prompt, i):
    a = ""
    display_answers(prompt, persons[i].name, names)
    check = True
    while check:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                screen.fill((250,250,250))
                display_answers(prompt, persons[i].name, names)
                if evt.key == K_BACKSPACE:
                    a = a[:-1]
                elif evt.key == K_RETURN:
                    check = False
                else:
                    a += evt.unicode
            elif evt.type == QUIT:
                return
        block = font.render(a, True, (blue))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()
    return a

        
def get_answers(prompt):
    answers = [0] * len(persons)
    for i in range(len(persons)):
        a = ""
        while (a not in true) and (a not in false):
            a = get_a(prompt,i)
            if a in false:
                persons[i].points -= 1
    for person in persons:
        if person.points <= 0:
            persons.remove(person)  
    return answers


def print_name(person, x_name, y_name):
    font = pygame.font.Font('freesansbold.ttf', 18)
    text = font.render(person.name + ": " + str(person.points), True, black, white) 
    textRect = text.get_rect()  
    textRect.center = (x_name, y_name)
    screen.blit(text, textRect)
    pygame.display.update()


def display_names():
    x_name = x/10
    y_name = y / 10
    
    for person in persons:
        print_name(person, x_name, y_name)
        x_name += x/len(persons)



def display_winner():
    screen.fill(white)
    pygame.display.update()
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render("Congratulations " + persons[0].name, True, blue, white) 
    textRect = text.get_rect()  
    textRect.center = (x//2, y//2)
    screen.blit(text, textRect)
    pygame.display.update()

class Person:
    def __init__(self, name, points):
        self.name = name
        self.points = points



### MAIN
num = get_num_players()
names = get_names()

while len(persons) > 1:
    for person in persons:
        prompt = get_question(person.name)
        answers = get_answers(prompt)
        print(answers)



display_winner()





