'''#modules
import pygame  
import sys
import os

#from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()  

#colors
white = (226, 229, 222)

#dimensions
height = 500 
width = 250

#display
screen = pygame.display.set_mode((height, width))  
pygame.display.set_caption('HAND CRICKET') 

#images
bg = pygame.image.load(r"Hand Cricket\title_1.png")
bg_blur = pygame.image.load(r"Hand Cricket\bg_blur.png")
play_button = pygame.image.load(r"Hand Cricket\buttons\play.png")
exit_button = pygame.image.load(r"Hand Cricket\buttons\leave.png")
how_to_button = pygame.image.load(r"Hand Cricket\buttons\how_to_play.png")
rules = pygame.image.load(r"Hand Cricket\rules.png")
back = pygame.image.load(r"Hand Cricket\buttons\back.png")

r = 0
screen_num = 0

def screens():
    global r
    
    screen.fill(white)  
    screen.blit(bg, (0, 0))  
    screen.blit(play_button, (198, 150))
    screen.blit(exit_button, (50, 150))
    screen.blit(how_to_button, (350, 150))

    if r == 1:
        screen.blit(bg_blur, (0, 0))
        screen.blit(back, (25, 15))
        pygame.display.update()

    if r == 2:
        screen.blit(rules, (0,0))
        pygame.display.update()

def screen_1():
    global r
    global screen_num

    #start game
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

        x , y = pygame.mouse.get_pos()
        
        if exit_button.get_rect().collidepoint(x-175 , y-150):
            r = 1
            screens()

    #rules
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

        x , y = pygame.mouse.get_pos()

        if exit_button.get_rect().collidepoint(x-300 , y-150):
            r = 2
            screens()

    #quit
    if event.type==pygame.QUIT:
        pygame.mixer.music.stop()
        pygame.quit()
        quit()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  

        x , y = pygame.mouse.get_pos()

        if exit_button.get_rect().collidepoint(x-50 , y-150):
            pygame.mixer.music.stop()
            pygame.quit()  
            quit()

def screen_2():
    global screen_num

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  

        x , y = pygame.mouse.get_pos()

        if exit_button.get_rect().collidepoint(x-350 , y-150):
            screens()

    if event.type==pygame.QUIT:
        pygame.mixer.music.stop()
        pygame.quit()
        quit()

while True:
    
    #60 fps
    clock.tick(60)
    
    for event in pygame.event.get():

        screens()

        #music
        pygame.mixer.music.load("Hand Cricket\Wii_music.mp3")
        pygame.mixer.music.play(-1)
        
        #screens
        screen_1()

        #exit
        if event.type==pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            quit()
    pygame.display.update()'''
#modules
import pygame  
import sys
import os

#from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()  

#colors
white = (226, 229, 222)

#dimensions
height = 500 
width = 250

#display
screen = pygame.display.set_mode((height, width))  
pygame.display.set_caption('HAND CRICKET') 

#images
bg = pygame.image.load(r"Hand Cricket\title_1.png")
bg_blur = pygame.image.load(r"Hand Cricket\bg_blur.png")
play_button = pygame.image.load(r"Hand Cricket\buttons\play.png")
exit_button = pygame.image.load(r"Hand Cricket\buttons\leave.png")
how_to_button = pygame.image.load(r"Hand Cricket\buttons\how_to_play.png")
rules = pygame.image.load(r"Hand Cricket\rules.png")
back = pygame.image.load(r"Hand Cricket\buttons\back.png")

r = 0
screen_num = 0

def screens():
    global r
    
    screen.fill(white)  
    screen.blit(bg, (0, 0))  
    screen.blit(play_button, (198, 150))
    screen.blit(exit_button, (50, 150))
    screen.blit(how_to_button, (350, 150))

    if r == 1:
        screen.blit(bg_blur, (0, 0))
        screen.blit(back, (25, 15))
        pygame.display.update()

    if r == 2:
        screen.blit(rules, (0,0))
        pygame.display.update()

def screen_1():
    global r
    global screen_num

    #start game
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

        x , y = pygame.mouse.get_pos()
        
        if exit_button.get_rect().collidepoint(x-175 , y-150):
            r = 1
            screens()

    #rules
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:

        x , y = pygame.mouse.get_pos()

        if exit_button.get_rect().collidepoint(x-300 , y-150):
            r = 2
            screens()

    #quit
    if event.type==pygame.QUIT:
        pygame.mixer.music.stop()
        pygame.quit()
        quit()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  

        x , y = pygame.mouse.get_pos()

        if exit_button.get_rect().collidepoint(x-50 , y-150):
            pygame.mixer.music.stop()
            pygame.quit()  
            quit()

def screen_2():
    global screen_num

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  

        x , y = pygame.mouse.get_pos()

        if exit_button.get_rect().collidepoint(x-350 , y-150):
            screens()

    if event.type==pygame.QUIT:
        pygame.mixer.music.stop()
        pygame.quit()
        quit()

while True:
    
    #60 fps
    clock.tick(60)
    
    for event in pygame.event.get():

        screens()

        #music
        pygame.mixer.music.load("Hand Cricket\Wii_music.mp3")
        pygame.mixer.music.play(-1)
        
        #screens
        screen_1()

        #exit
        if event.type==pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            quit()
    pygame.display.update()