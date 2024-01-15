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
player = 1

for i in range(8):
    row=[None]*8
    markers.append(row)

markers[3][3] = markers[4][4] =-1
markers[3][4] = markers[4][3] = 1
possibles = get_possibles(markers,player)

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
    cont_blacks=0
    cont_white=0
    x_pos=0
    for x in markers:
        y_pos = 0
        for y in x:
            if y==1:
                pygame.draw.circle(screen,(0,0,0),(x_pos*100+50,y_pos*100+50),40)
                cont_blacks = 0
            if y==-1:
                pygame.draw.circle(screen,(255,255,255),(x_pos*100+50,y_pos*100+50),40)
                cont_white = 0
            y_pos+=1
        x_pos +=1

def count_markers():
    cont_blacks=0
    cont_white=0
    x_pos=0
    for x in markers:
        y_pos = 0
        for y in x:
            if y==1:
                cont_blacks += 1
            if y==-1:
                cont_white += 1
            y_pos+=1
        x_pos +=1
    print ("Blacks: ",cont_blacks, " Whites: ", cont_white)   

def draw_possibles(player,possibles):
    x_pos=0
    for x in possibles:
        y_pos = 0
        for y in x:
            if y is not None:
                pygame.draw.circle(screen,(0,0,0) if player==1 else (255,255,255),(x_pos*100+50,y_pos*100+50),40,2)
            y_pos += 1
        x_pos += 1

def count_possibles(): 
    count=0
    for x in possibles:
        for y in x:
            if y is not None:
                count += 1
    return count

run = True
while run:
    draw_grid()
    draw_markers()
    draw_possibles(player,possibles)  
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
            if possibles[cell_x][cell_y] is not None: 
            # if markers[cell_x][cell_y] is None:
                markers[cell_x][cell_y] = player
                get_new_markers(markers,player,pos=(cell_x,cell_y))
                player *=-1
                possibles = get_possibles(markers,player)
                if count_possibles()==0:
                    print("No más movimientos para ", "negro" if player==1 else "blanco")
                    player*=-1
                    possibles = get_possibles(markers,player)
                print(count_possibles())
                count_markers()
    pygame.display.update()

pygame.quit()