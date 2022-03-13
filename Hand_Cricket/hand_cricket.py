def handcricket(id): 
    global score
    import sys
    import pygame  
    import random
    import time
    #from pygame.locals import *

    #pygame clock
    clock = pygame.time.Clock()

    #game initialisation
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
    bg_blur = pygame.image.load(r"Hand_Cricket\bg_blur.png")

    #numbers
    one_image = pygame.image.load(r"Hand_Cricket\buttons\one.png")
    two_image = pygame.image.load(r"Hand_Cricket\buttons\two.png")
    three_image = pygame.image.load(r"Hand_Cricket\buttons\three.png")
    four_image = pygame.image.load(r"Hand_Cricket\buttons\four.png")
    five_image = pygame.image.load(r"Hand_Cricket\buttons\five.png")
    six_image = pygame.image.load(r"Hand_Cricket\buttons\six.png")
    seven_image = pygame.image.load(r"Hand_Cricket\buttons\seven.png")
    eight_image = pygame.image.load(r"Hand_Cricket\buttons\eight.png")
    nine_image = pygame.image.load(r"Hand_Cricket\buttons\nine.png")
    ten_image = pygame.image.load(r"Hand_Cricket\buttons\ten.png")

    #out
    out1 = pygame.image.load(r"Hand_Cricket\out1.png")
    out2 = pygame.image.load(r"Hand_Cricket\out2.png")
    out3 = pygame.image.load(r"Hand_Cricket\out3.png")
    out4 = pygame.image.load(r"Hand_Cricket\out4.png")
    out5 = pygame.image.load(r"Hand_Cricket\out5.png")
    out6 = pygame.image.load(r"Hand_Cricket\out6.png")
    out7 = pygame.image.load(r"Hand_Cricket\out7.png")

    #other images
    equal = pygame.image.load(r"Hand_Cricket\equal_to.png")
    total = pygame.image.load(r"Hand_Cricket\total.png")
    exit_button = pygame.image.load(r"Hand_Cricket\buttons\leave.png")

    #screen1
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

    #screen2
    def screen2():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if exit_button.get_rect().collidepoint(x-25,y-250):
                pygame.quit()
                quit()

    #out = 0
    r = int(random.randint(1,7))
    def outscreen(r):
        #global out
        #r = int(random.randint(1,7))

        if r == 1:
            screen.blit(out1, (0,0))
            pygame.display.update()
            print(score)
            time.sleep(2)
            sys.exit()

        elif r == 2:
            screen.blit(out2, (0,0))
            pygame.display.update()
            print(score)
            time.sleep(2)
            sys.exit()

        elif r == 3:
            screen.blit(out3, (0,0))
            pygame.display.update()
            print(score)
            time.sleep(2)
            sys.exit()

        elif r == 4:
            screen.blit(out4, (0,0))
            pygame.display.update()
            print(score)
            time.sleep(2)
            sys.exit()

        elif r == 5:
            screen.blit(out5, (0,0))
            pygame.display.update()
            print(score)
            time.sleep(2)
            sys.exit()

        elif r == 6:
            screen.blit(out6, (0,0))
            pygame.display.update()
            print(score)
            time.sleep(2)
            sys.exit()


        elif r == 7:
            screen.blit(out7, (0,0))
            pygame.display.update()
            print(score)
            time.sleep(2)
            sys.exit()
        
        #out = 1

    def gameplay(a):
        #global out
        global score
        b = int(random.randint(1,10))
        #n = 0
        while True:
            #n += 1
            if a == b:
                outscreen(r)
            else:
                score = score + a
                font()
            break
        #balls = n

    #variables
    a = 0
    score = 0

    def player():
        global a
        global score

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if one_image.get_rect().collidepoint(x-25,y-25):
                a = 1
                gameplay(a)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if two_image.get_rect().collidepoint(x-125,y-25):
                a = 2
                gameplay(a)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if three_image.get_rect().collidepoint(x-225,y-25):
                a = 3
                gameplay(a)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if four_image.get_rect().collidepoint(x-325,y-25):
                a = 4
                gameplay(a)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if five_image.get_rect().collidepoint(x-425,y-25):
                a = 5
                gameplay(a)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if six_image.get_rect().collidepoint(x-25,y-125):
                a = 6
                gameplay(a)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if seven_image.get_rect().collidepoint(x-125,y-125):
                a = 7
                gameplay(a)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if eight_image.get_rect().collidepoint(x-225,y-125):
                a = 8
                gameplay(a)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if nine_image.get_rect().collidepoint(x-325,y-125):
                a = 9
                gameplay(a)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x , y = pygame.mouse.get_pos()
            if ten_image.get_rect().collidepoint(x-425,y-125):
                a = 10
                gameplay(a)
        
    def font():
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        text = myfont.render(str(score), True, white)
        screen.blit(text, (425,250))
        pygame.display.update()

    def game():
        screen1()
        screen2()
        player()

    def leave():
        if event.type == pygame.QUIT:
            pygame.quit()
            

    run = True
    while run:
        
        #60 fps
        clock.tick(60)
        
        for event in pygame.event.get():
            mouse = event.type == pygame.MOUSEMOTION
            if mouse == False:
                game()

            leave()
                
        pygame.display.update()
handcricket(id)