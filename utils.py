# import pygame
from pygame.locals import *




def up_search(markers,player,x_pos,y_pos,possibles):
    # print("-"*20)
    if y_pos>=2 and markers[x_pos][y_pos-1] == player*-1:
        for y in reversed(range(0,y_pos-1)):
            if markers[x_pos][y] is None:
                # print("Acá puede ser, arriba:",x_pos, y )
                possibles[x_pos][y] = player*2
                return (x_pos,y)
            if markers[x_pos][y] == player:
                return
            if markers[x_pos][y] == player*-1:
                continue
    return

def down_search(markers,player,x_pos,y_pos,possibles):
    # print("-"*20)
    if y_pos<=5 and markers[x_pos][y_pos+1] == player*-1:
        for y in range(y_pos+2,8):
            if markers[x_pos][y] is None:
                # print("Acá puede ser, abajo:",x_pos, y )
                possibles[x_pos][y] = player*2
                return (x_pos,y)
            if markers[x_pos][y] == player:
                return
            if markers[x_pos][y] == player*-1:
                continue
    return

def right_search(markers,player,x_pos,y_pos,possibles):
    # print("-"*20)
    if x_pos<5 and markers[x_pos+1][y_pos] == player*-1:
        for x in range(x_pos+2,8):
            if markers[x][y_pos] is None:
                # print("Acá puede ser derecha:, ",x, y_pos)
                possibles[x][y_pos] = player*2
                return (x,y_pos)
            if markers[x][y_pos] == player:
                return
            if markers[x][y_pos] == player*-1:
                continue
    return
        
def left_search(markers,player,x_pos,y_pos,possibles):
    # print("-"*20)
    if x_pos>2 and markers[x_pos-1][y_pos] == player*-1:
        for x in reversed(range(0,x_pos-1)):
            if markers[x][y_pos] is None:
                # print("Acá puede ser, izquierda ",x, y_pos )
                possibles[x][y_pos] = player*2
                return (x,y_pos)
            if markers[x][y_pos] == player:
                return
            if markers[x][y_pos] == player*-1:
                continue
    return

def up_left_search(markers,player,x_pos,y_pos,possibles):
    if markers[x_pos-1][y_pos-1] == player*-1:
        x_iter = list(reversed(range(0,x_pos-1)))
        y_iter = list(reversed(range(0,y_pos-1)))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] is None:
                # print("Acá puede ser, arriba izq:",xy[0],xy[1] )
                possibles[xy[0]][xy[1]]  = player*2
                return (xy[0],xy[1])
            if markers[xy[0]][xy[1]] == player:
                return
            if markers[xy[0]][xy[1]] == player*-1:
                continue
    return

def up_right_search(markers,player,x_pos,y_pos,possibles):
    if markers[x_pos+1][y_pos-1] == player*-1:
        x_iter = list(range(x_pos+2,8))
        y_iter = list(reversed(range(0,y_pos-1)))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        # print("xy iter: ", xy_iter)
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] is None:
                # print("Acá puede ser, arriba izq:",xy[0],xy[1] )
                possibles[xy[0]][xy[1]]  = player*2
                return (xy[0],xy[1])
            if markers[xy[0]][xy[1]] == player:
                return
            if markers[xy[0]][xy[1]] == player*-1:
                continue
    return



def get_possibles(markers,player):
    possibles = []
    for i in range(8):
        row=[None]*8
        possibles.append(row)

    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == player:
                up_search(markers,player,x_pos,y_pos,possibles)
                down_search(markers,player,x_pos,y_pos,possibles)
                right_search(markers,player,x_pos,y_pos,possibles)
                left_search(markers,player,x_pos,y_pos,possibles)
                up_left_search(markers,player,x_pos,y_pos,possibles)
                up_right_search(markers,player,x_pos,y_pos,possibles)
                # print("terminé busqueda", "-"*30)
            y_pos += 1
        x_pos += 1

    
    # for row in possibles:
    #     print(row)

    return possibles


