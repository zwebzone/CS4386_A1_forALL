import sys
import pygame
from math import sqrt as sqrt

import time
n_gezi=6

WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255,0,0
GREEN = 0,255,0
size = width, height = 480, 480
size_plus = 480, 580
cell_width = (width/n_gezi)
cell_height = (height/n_gezi)
font_size = 60

def init():
    pygame.init()
    #screen = pygame.display.set_mode(size)
    screen = pygame.display.set_mode(size_plus)# (size)
    screen.fill(WHITE)

    # Horizontal lines
    for i in range(0, 7):
        pygame.draw.line(screen, BLACK, [0, (cell_height)*i], [width, ((cell_height)*i)], 3)
    # Vertical lines
    for i in range(0, 7):
        pygame.draw.line(screen, BLACK, [(cell_width)*i, 0], [((cell_width)*i), height], 3)
    # black-white    
    for i in range(0, 6):
        for j in range(0, 6):
            if (i+j)%2==0:
                pygame.draw.rect(screen, BLACK, pygame.Rect((cell_width)*i, (cell_height)*j, cell_width, cell_height))
    return screen

def clearScreen(screen):
    screen.fill(WHITE)

    # Horizontal lines
    for i in range(0, 7):
        pygame.draw.line(
            screen, BLACK, [0, (cell_height)*i], [width, ((cell_height)*i)], 3)
    # Vertical lines
    for i in range(0, 7):
        pygame.draw.line(
            screen, BLACK, [(cell_width)*i, 0], [((cell_width)*i), height], 3)
    for i in range(0, 6):
        for j in range(0, 6):
            if (i+j)%2==0:
                pygame.draw.rect(screen, BLACK, pygame.Rect((cell_width)*i, (cell_height)*j, cell_width, cell_height))
    

def getCell(pos):
    a= '{:g}'.format(pos[0]//cell_width)
    b= '{:g}'.format(pos[1]//cell_height)

    return(int(b),int(a))
##    if(pos[0] >= 0 and pos[0] < width/3 and pos[1] >= 0 and pos[1] < height/3):
##        return (0, 0)
##    if(pos[0] >= width/3 and pos[0] < (width/3)*2 and pos[1] >= 0 and pos[1] < height/3):
##        return (0, 1)
##    if(pos[0] >= (width/3)*2 and pos[0] < width and pos[1] >= 0 and pos[1] < height/3):
##        return (0, 2)
##    if(pos[0] >= 0 and pos[0] < width/3 and pos[1] >= height/3 and pos[1] < (height/3)*2):
##        return (1, 0)
##    if(pos[0] >= width/3 and pos[0] < (width/3)*2 and pos[1] >= height/3 and pos[1] < (height/3)*2):
##        return (1, 1)
##    if(pos[0] >= (width/3)*2 and pos[0] < width and pos[1] >= height/3 and pos[1] < (height/3)*2):
##        return (1, 2)
##    if(pos[0] >= 0 and pos[0] < width/3 and pos[1] >= (height/3)*2 and pos[1] < height):
##        return (2, 0)
##    if(pos[0] >= width/3 and pos[0] < (width/3)*2 and pos[1] >= (height/3)*2 and pos[1] < height):
##        return (2, 1)
##    if(pos[0] >= (width/3)*2 and pos[0] < width and pos[1] >= (height/3)*2 and pos[1] < height):
##        return (2, 2)

def drawSymbole(screen, cell, symbole):  
    if(symbole == "X"):
        x00 = int(((cell_width)*cell[1]))
        y00 = int(((cell_height)*cell[0]))
        pygame.draw.circle(screen, GREEN, (x00+cell_width/2,y00+cell_width/2), cell_width/4)
    elif(symbole == "O"):
        x00 = int(((cell_width)*cell[1]))
        y00 = int(((cell_height)*cell[0]))
        pygame.draw.circle(screen, RED, (x00+cell_width/2,y00+cell_width/2), cell_width/4)  
    refresh()

def playerInput(screen):
    running = True
    while running:
        for event in pygame.event.get():
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                cell = getCell(pos)
                return cell[0], cell[1]
            if event.type == pygame.QUIT:
                running = False
            refresh()
    pygame.quit()  # quits pygame
    sys.exit()

def ask(screen, question, line=2):
    running = True
    # "ask(screen, question) -> answer"
    pygame.font.init()
    writeScreen(screen, question, line=line)
    center_yes_x = width/4
    center_yes_y = height/4
    center_no_x = (width/4)*2
    center_no_y = (height/4)
    while running:
        for event in pygame.event.get():
            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                return
            if event.type == pygame.QUIT:
                running = False
            refresh()
    pygame.quit()
    sys.exit()

def writeScreen(screen, txt, line=1):
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("monospace", font_size)

    # render text
    label = myfont.render(txt, 50, (0,200,0))
    screen.blit(label, ((width/2)-(font_size/3)*len(txt), (height/4)*line))
    refresh()
def writeScreen_4_show(screen, txt, line=1):
    screen.fill(WHITE, (0, 480, screen.get_width(), screen.get_height()// 5))
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("monospace", 20)

    # render text
    label = myfont.render(txt, 50, (0,255,0))
    screen.blit(label, (64, 548))
    # screen.blit(label, ((width/0.8)-(font_size/2.8)*len(txt), (height/3.5)*line))
    refresh()

def refresh():
    pygame.display.update()
    
