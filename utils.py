def up_search(markers,player,x_pos,y_pos,possibles):
    if y_pos>=2 and markers[x_pos][y_pos-1] == player*-1:
        for y in reversed(range(0,y_pos-1)):
            if markers[x_pos][y] is None:
                possibles[x_pos][y] = player*2
                return (x_pos,y)
            if markers[x_pos][y] == player:
                return
            if markers[x_pos][y] == player*-1:
                continue
    return

def down_search(markers,player,x_pos,y_pos,possibles):
    if y_pos<=5 and markers[x_pos][y_pos+1] == player*-1:
        for y in range(y_pos+2,8):
            if markers[x_pos][y] is None:
                possibles[x_pos][y] = player*2
                return (x_pos,y)
            if markers[x_pos][y] == player:
                return
            if markers[x_pos][y] == player*-1:
                continue
    return

def right_search(markers,player,x_pos,y_pos,possibles):
    if x_pos<=5 and markers[x_pos+1][y_pos] == player*-1:
        for x in range(x_pos+2,8):
            if markers[x][y_pos] is None:
                possibles[x][y_pos] = player*2
                return (x,y_pos)
            if markers[x][y_pos] == player:
                return
            if markers[x][y_pos] == player*-1:
                continue
    return
        
def left_search(markers,player,x_pos,y_pos,possibles):
    if x_pos>=2 and markers[x_pos-1][y_pos] == player*-1:
        for x in reversed(range(0,x_pos-1)):
            if markers[x][y_pos] is None:
                possibles[x][y_pos] = player*2
                return (x,y_pos)
            if markers[x][y_pos] == player:
                return
            if markers[x][y_pos] == player*-1:
                continue
    return

def up_left_search(markers,player,x_pos,y_pos,possibles):
    if x_pos>=2 and y_pos>=2 and markers[x_pos-1][y_pos-1] == player*-1:
        x_iter = list(reversed(range(0,x_pos-1)))
        y_iter = list(reversed(range(0,y_pos-1)))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] is None:
                possibles[xy[0]][xy[1]]  = player*2
                return (xy[0],xy[1])
            if markers[xy[0]][xy[1]] == player:
                return
            if markers[xy[0]][xy[1]] == player*-1:
                continue
    return

def up_right_search(markers,player,x_pos,y_pos,possibles):
    if x_pos<=5 and y_pos>=2 and markers[x_pos+1][y_pos-1] == player*-1:
        x_iter = list(range(x_pos+2,8))
        y_iter = list(reversed(range(0,y_pos-1)))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] is None:
                possibles[xy[0]][xy[1]]  = player*2
                return (xy[0],xy[1])
            if markers[xy[0]][xy[1]] == player:
                return
            if markers[xy[0]][xy[1]] == player*-1:
                continue
    return

def down_right_search(markers,player,x_pos,y_pos,possibles):
    if x_pos<=5 and y_pos<=5 and markers[x_pos+1][y_pos+1] == player*-1:
        x_iter = list(range(x_pos+2,8))
        y_iter = list(range(y_pos+2,8))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] is None:
                possibles[xy[0]][xy[1]]  = player*2
                return (xy[0],xy[1])
            if markers[xy[0]][xy[1]] == player:
                return
            if markers[xy[0]][xy[1]] == player*-1:
                continue
    return

def down_left_search(markers,player,x_pos,y_pos,possibles):
    if x_pos>=1 and y_pos<=5 and markers[x_pos-1][y_pos+1] == player*-1:
        x_iter = list(reversed(range(0,x_pos-1)))
        y_iter = list(range(y_pos+2,8))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] is None:
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
                down_right_search(markers,player,x_pos,y_pos,possibles)
                down_left_search(markers,player,x_pos,y_pos,possibles)
                
            y_pos += 1
        x_pos += 1

    
    # for row in possibles:
    #     print(row)

    return possibles


def up_change(markers,player,pos):
    changes = []
    if pos[1]>=2 and markers[pos[0]][pos[1]-1] == player*-1:
        for y in list(reversed(range(0,pos[1]))):
            if markers[pos[0]][y] == player*-1:
                changes.append((pos[0],y))
            elif markers[pos[0]][y] == player:
                break
            elif markers[pos[0]][y] is None:
                changes = []
                break
        
    return changes

def down_change(markers,player,pos):
    changes = []
    if pos[1]<=5 and markers[pos[0]][pos[1]+1] == player*-1:
        for y in range(pos[1]+1,8):
            if markers[pos[0]][y] == player*-1:
                changes.append((pos[0],y))
            elif markers[pos[0]][y] == player:
                break
            elif markers[pos[0]][y] is None:
                changes = []
                break
    return changes

def right_change(markers,player,pos):
    changes = []
    if pos[0]<=5 and markers[pos[0]+1][pos[1]] == player*-1:
        for x in range(pos[0]+1,8):
            if markers[x][pos[1]] == player*-1:
                changes.append((x,pos[1]))
            elif markers[x][pos[1]] == player:
                break
            elif markers[x][pos[1]] is None:
                changes = []
                break
    return changes

def left_change(markers,player,pos):
    changes = []
    if pos[0]>=2 and markers[pos[0]-1][pos[1]] == player*-1:
        for x in list(reversed(range(0,pos[0]))):
            if markers[x][pos[1]] == player*-1:
                changes.append((x,pos[1]))
            elif markers[x][pos[1]] == player:
                break
            elif markers[x][pos[1]] is None:
                changes = []
                break
    return changes

def up_left_change(markers,player,pos):
    changes = []
    if pos[0]>=2 and pos[1]>=2 and markers[pos[0]-1][pos[1]-1] == player*-1:
        x_iter = list(reversed(range(0,pos[0])))
        y_iter = list(reversed(range(0,pos[1])))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] == player*-1:
                changes.append((xy[0],xy[1]))
            elif markers[xy[0]][xy[1]] == player:
                break
            elif markers[xy[0]][xy[1]] is None:
                changes = []
                break
    return changes

def up_right_change(markers,player,pos):
    changes = []
    if pos[0]<=5 and pos[1]>=2 and markers[pos[0]+1][pos[1]-1] == player*-1:
        x_iter = list(range(pos[0]+1,8))
        y_iter = list(reversed(range(0,pos[1])))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] == player*-1:
                changes.append((xy[0],xy[1]))
            elif markers[xy[0]][xy[1]] == player:
                break
            elif markers[xy[0]][xy[1]] is None:
                changes = []
                break
    return changes

def down_right_change(markers,player,pos):
    changes = []
    if pos[0]<=5 and pos[1]<=5 and markers[pos[0]+1][pos[1]+1] == player*-1:
        x_iter = list(range(pos[0]+1,8))
        y_iter = list(range(pos[1]+1,8))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] == player*-1:
                changes.append((xy[0],xy[1]))
            elif markers[xy[0]][xy[1]] == player:
                break
            elif markers[xy[0]][xy[1]] is None:
                changes = []
                break
    return changes

def down_left_change(markers,player,pos):
    changes = []
    if pos[0]>=2 and pos[1]<=5 and markers[pos[0]-1][pos[1]+1] == player*-1:
        x_iter = list(reversed(range(0,pos[0])))
        y_iter = list(range(pos[1]+1,8))
        xy_iter = [ (x_iter[i],y_iter[i]) for i in range(min(len(x_iter),len(y_iter))) ]
        for xy in xy_iter:
            if markers[xy[0]][xy[1]] == player*-1:
                changes.append((xy[0],xy[1]))
            elif markers[xy[0]][xy[1]] == player:
                break
            elif markers[xy[0]][xy[1]] is None:
                changes = []
                break
    return changes


def get_new_markers(markers,player,pos):
    # print("nuevo ", "negro" if player==1 else "blanco", "en", pos[0],pos[1] )
    to_change=[]
    to_change += up_change(markers,player,pos)
    to_change += down_change(markers,player,pos)
    to_change += right_change(markers,player,pos)
    to_change += left_change(markers,player,pos)
    to_change += up_left_change(markers,player,pos)
    to_change += up_right_change(markers,player,pos)
    to_change += down_right_change(markers,player,pos)
    to_change += down_left_change(markers,player,pos)

    for i in to_change:
        markers[i[0]][i[1]] = player

    return