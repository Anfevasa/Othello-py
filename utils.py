def draw_possibles(markers, player):
    # print("*"*20)
    possibles = []
    for i in range(8):
        row=[None]*8
        possibles.append(row)
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == player:
                print("Encontrado, ","negro" if player==1 else "blanco"," en ", x_pos,y_pos)
                busqueda(markers,player,x_pos,y_pos);
            y_pos += 1
        x_pos += 1


def up_search(markers,player,x_pos,y_pos):
    # print("-"*20)
    if y_pos>=2 and markers[x_pos][y_pos-1] == player*-1:
        for y in reversed(range(0,y_pos-1)):
            if markers[x_pos][y] is None:
                print("Acá puede ser, arriba:",x_pos, y )
                return (x_pos,y)
            if markers[x_pos][y] == player:
                return
            if markers[x_pos][y] == player*-1:
                continue
    return

def down_search(markers,player,x_pos,y_pos):
    # print("-"*20)
    if y_pos<=5 and markers[x_pos][y_pos+1] == player*-1:
        for y in range(y_pos+2,8):
            if markers[x_pos][y] is None:
                print("Acá puede ser, abajo:",x_pos, y )
                return (x_pos,y)
            if markers[x_pos][y] == player:
                return
            if markers[x_pos][y] == player*-1:
                continue
    return

def right_search(markers,player,x_pos,y_pos):
    # print("-"*20)
    if x_pos<5 and markers[x_pos+1][y_pos] == player*-1:
        for x in range(x_pos+2,8):
            if markers[x][y_pos] is None:
                print("Acá puede ser derecha:, ",x, y_pos)
                return (x,y_pos)
            if markers[x][y_pos] == player:
                return
            if markers[x][y_pos] == player*-1:
                continue
    return
        
def left_search(markers,player,x_pos,y_pos):
    # print("-"*20)
    if x_pos>2 and markers[x_pos-1][y_pos] == player*-1:
        for x in reversed(range(0,x_pos-1)):
            if markers[x][y_pos] is None:
                print("Acá puede ser, izquierda ",x, y_pos )
                return (x,y_pos)
            if markers[x][y_pos] == player:
                return
            if markers[x][y_pos] == player*-1:
                continue
    return

def up_left_search(markers,player,x_pos,y_pos):
    if markers[x_pos-1][y_pos-1] == player*-1:
        # x_iter = 
        for y in reversed(range(0,y_pos-1)):
            if markers[x_pos][y] is None:
                print("Acá puede ser, arriba:",x_pos, y )
                return (x_pos,y)
            if markers[x_pos][y] == player:
                return
            if markers[x_pos][y] == player*-1:
                continue
    return



def busqueda(markers,player,x_pos,y_pos):
    up_search(markers,player,x_pos,y_pos)
    down_search(markers,player,x_pos,y_pos)
    right_search(markers,player,x_pos,y_pos)
    left_search(markers,player,x_pos,y_pos)


