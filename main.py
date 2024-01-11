import pygame
from pygame.locals import *
from utils import *

pygame.init()

screen_width = 800
screen_height = 800

line_width =2
clicked=False
pos=[]
markers = []
possibles = []
player = 1

for i in range(8):
    row=[None]*8
    markers.append(row)
    possibles.append(row)

def print_board():
    for row in markers:
        print(row)

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Othello")

def draw_grid():
    bg=(4,134,71)
    grid = (0,0,0)
    screen.fill(bg)
    for x in range(1,9):
        pygame.draw.line(screen,grid,(0,x*100),(screen_width,x*100),line_width)
        pygame.draw.line(screen,grid,(x*100,0),(x*100,screen_width),line_width)

def draw_markers():
    x_pos=0
    for x in markers:
        y_pos = 0
        for y in x:
            if y==1:
                pygame.draw.circle(screen,(0,0,0),(x_pos*100+50,y_pos*100+50),40)
            if y==-1:
                pygame.draw.circle(screen,(255,255,255),(x_pos*100+50,y_pos*100+50),40)
            y_pos+=1
        x_pos +=1


run = True
while run:
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked==False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked==True:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]//100
            cell_y = pos[1]//100
            if markers[cell_x][cell_y] is None:
                markers[cell_x][cell_y] = player
                draw_possibles(markers,player)  
                player *=-1
                # print_board()
    pygame.display.update()

pygame.quit()