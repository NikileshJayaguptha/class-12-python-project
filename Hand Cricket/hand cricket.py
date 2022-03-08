#modules
import pygame  
import random
import sys
import os

#from pygame.locals import *
clock = pygame.time.Clock()
pygame.init()  

#colors
white = (226, 229, 222)

#dimensions
height = 600 
width = 350

#display
screen = pygame.display.set_mode((height, width))  
pygame.display.set_caption('HAND CRICKET') 

#images
bg_blur = pygame.image.load(r"Hand Cricket\bg_blur.png")

#numbers
one_image = pygame.image.load(r"Hand Cricket\buttons\one.png")
two_image = pygame.image.load(r"Hand Cricket\buttons\two.png")
three_image = pygame.image.load(r"Hand Cricket\buttons\three.png")
four_image = pygame.image.load(r"Hand Cricket\buttons\four.png")
five_image = pygame.image.load(r"Hand Cricket\buttons\five.png")
six_image = pygame.image.load(r"Hand Cricket\buttons\six.png")
seven_image = pygame.image.load(r"Hand Cricket\buttons\seven.png")
eight_image = pygame.image.load(r"Hand Cricket\buttons\eight.png")
nine_image = pygame.image.load(r"Hand Cricket\buttons\nine.png")
ten_image = pygame.image.load(r"Hand Cricket\buttons\ten.png")

#out
out1 = pygame.image.load(r"Hand Cricket\out1.png")
out2 = pygame.image.load(r"Hand Cricket\out2.png")
out3 = pygame.image.load(r"Hand Cricket\out3.png")
out4 = pygame.image.load(r"Hand Cricket\out4.png")
out5 = pygame.image.load(r"Hand Cricket\out5.png")
out6 = pygame.image.load(r"Hand Cricket\out6.png")
out7 = pygame.image.load(r"Hand Cricket\out7.png")

equal = pygame.image.load(r"Hand Cricket\equal_to.png")
total = pygame.image.load(r"Hand Cricket\total.png")
exit_button = pygame.image.load(r"Hand Cricket\buttons\leave.png")

def screen1():

    screen.fill(white)  
    screen.blit(bg_blur, (0, 0))

    #numbers display
    screen.blit(one_image, (20,20))
    screen.blit(two_image, (120,20))
    screen.blit(three_image, (220,20))
    screen.blit(four_image, (320,20))
    screen.blit(five_image, (420,20))
    screen.blit(six_image, (20,120))
    screen.blit(seven_image, (120,120))
    screen.blit(eight_image, (220,120))
    screen.blit(nine_image, (320,120))
    screen.blit(ten_image, (420,120))

    screen.blit(equal, (375,275))
    screen.blit(total, (220,260))
    screen.blit(exit_button, (20, 250))

def screen2():
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if exit_button.get_rect().collidepoint(x-25,y-250):
            pygame.quit()
            quit()

def outscreen():
    r = int(random.randint(1,7))
    if r == 1:
        screen.blit(out1, (0,0))
    elif r == 2:
        screen.blit(out2, (0,0))
    elif r == 3:
        screen.blit(out3, (0,0))
    elif r == 4:
        screen.blit(out4, (0,0))
    elif r == 5:
        screen.blit(out5, (0,0))
    elif r == 6:
        screen.blit(out6, (0,0))
    elif r == 7:
        screen.blit(out7, (0,0))

def music():
    #music
    pygame.mixer.music.load("Hand Cricket\Wii_music.mp3")
    pygame.mixer.music.play(-1)

a = 0
score = 0
def player():
    global a
    global score
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if one_image.get_rect().collidepoint(x-25,y-25):
            a = 1
            gameplay()
    
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if two_image.get_rect().collidepoint(x-125,y-25):
            a = 2
            gameplay()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if three_image.get_rect().collidepoint(x-225,y-25):
            a = 3
            gameplay()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if four_image.get_rect().collidepoint(x-325,y-25):
            a = 4
            gameplay()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if five_image.get_rect().collidepoint(x-425,y-25):
            a = 5
            gameplay()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if six_image.get_rect().collidepoint(x-25,y-125):
            a = 6
            gameplay()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if seven_image.get_rect().collidepoint(x-125,y-125):
            a = 7
            gameplay()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if eight_image.get_rect().collidepoint(x-225,y-125):
            a = 8
            gameplay()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if nine_image.get_rect().collidepoint(x-325,y-125):
            a = 9
            gameplay()

    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        x , y = pygame.mouse.get_pos()
        if ten_image.get_rect().collidepoint(x-425,y-125):
            a = 10
            gameplay()
    
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    text = myfont.render(str(score), False, white)
    textRect = text.get_rect()
    screen.blit(text, textRect)
    pygame.display.update()

def gameplay():
    global a
    global score
    b = int(random.randint(1,10))
    #score = 0
    n = 0
    while True:
        n += 1
        if a == b:
            outscreen()
        else:
            score = score + a
    #balls = n
    

while True:
    
    #60 fps
    clock.tick(60)
    
    for event in pygame.event.get():
        
        screen1()
        screen2()
        player()
        
        
        #music

        #exit
        if event.type==pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            quit()
    pygame.display.update()