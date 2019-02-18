import sys
from random import randint
from collections import OrderedDict

#entrada = sys.argv[1]
entrada = "F21C856B49A73ED."
L = list(entrada)
#print(L)
estado_inicial_array = [0 if x=="." else int(x,16) for x in entrada]
estado_inicial = [estado_inicial_array[0:4],estado_inicial_array[4:8],estado_inicial_array[8:12],estado_inicial_array[12:16]]
goal_state = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
#print(estado_inicial)
fila_puntero = 0
columna_puntero = 0
fila_posicionfila = []
punishup = 0
punishdown = 0
punishleft  = 0
punishright = 0
##def calculo_heuristica(estado):
##    heuristica = 0
##    counter = 1
##    for i in range(4):
##        for j in range(4):
##            if(estado[i][j] != counter and estado[i][j] != 0 ):
##                heuristica +=1
##    
##            counter +=1
##    return heuristica

#usar manhattan
def calculo_heuristica(estado):
    global goal_state
    heuristica = 0
    for i in range(4):
        for j in range(4):
            value = estado[i][j]
            if(value != 0):
                targetX = (value - 1) / 4
                targetY = (value - 1) % 4
                dx = i - targetX
                dy = j - targetY
                heuristica += abs(dx) + abs(dy) 
                #heuristica += abs(goal_state[i][j] - estado[i][j])
    return heuristica
   

        
#huehue = calculo_heuristica(estado_inicial)
#print(huehue)
def find_empty_space(estado):
    for x in range(4):
        for y in range(4):
            if(estado[y][x] == 0):
                y_and_x = [y,x]
                #print(y_and_x)
    return y_and_x

def move_up(estado):
    global fila_puntero,columna_puntero
    fila_posicionfila = find_empty_space(estado_inicial)
    fila_puntero = fila_posicionfila[1]
    columna_puntero = fila_posicionfila[0]
    if(columna_puntero !=0):
        estado[columna_puntero][fila_puntero], estado[columna_puntero-1][fila_puntero] = estado[columna_puntero-1][fila_puntero], estado[columna_puntero][fila_puntero]
        return estado
    else:
        move = False
        return move
        
    

def move_down(estado):
    global fila_puntero,columna_puntero
    fila_posicionfila = find_empty_space(estado_inicial)
    fila_puntero = fila_posicionfila[1]
    columna_puntero = fila_posicionfila[0]
    if(columna_puntero !=3):
        estado[columna_puntero][fila_puntero], estado[columna_puntero+1][fila_puntero] = estado[columna_puntero+1][fila_puntero], estado[columna_puntero][fila_puntero]
        return estado
    else:
        move = False
        return move

def move_right(estado):
    global fila_puntero,columna_puntero
    fila_posicionfila = find_empty_space(estado_inicial)
    fila_puntero = fila_posicionfila[1]
    columna_puntero = fila_posicionfila[0]
    if(fila_puntero !=3):
        estado[columna_puntero][fila_puntero], estado[columna_puntero][fila_puntero+1] = estado[columna_puntero][fila_puntero+1], estado[columna_puntero][fila_puntero]
        return estado
    else:
        move = False
        return move

def move_left(estado):
    global fila_puntero,columna_puntero
    fila_posicionfila = find_empty_space(estado_inicial)
    fila_puntero = fila_posicionfila[1]
    columna_puntero = fila_posicionfila[0]
    
    if(fila_puntero !=0):
        estado[columna_puntero][fila_puntero], estado[columna_puntero][fila_puntero-1] = estado[columna_puntero][fila_puntero-1], estado[columna_puntero][fila_puntero]
        return estado
    else:
        move = False
        return move
def selector():
    global punishup, punishdown, punishleft, punishright
    #llamar a todos los moves
    subestado1 = move_up(estado_inicial)
    subestado2 = move_down(estado_inicial)
    subestado3 = move_right(estado_inicial)
    subestado4 = move_left(estado_inicial)
    try:
        h1 = calculo_heuristica(subestado1) 
    except:
        h1 = 700
    try:
        h2 = calculo_heuristica(subestado2) 
    except:
        h2 = 700
    try:
        h3 = calculo_heuristica(subestado3) 
    except:
        h3 = 700
    try:
        h4 = calculo_heuristica(subestado4) 
    except:
        h4 = 700
    hes = {}
    hes[1] = h1
    hes[2] = h2
    hes[3] = h3
    hes[4] = h4
    print(h1)
    print(h2)
    print(h3)
    print(h4)
    return hes

countup = 0
countdown = 0
countright = 0
countleft = 0

#while(np.array_equal(estado_inicial,goal_state) == False):
while(estado_inicial != goal_state):
    lmao = selector()
    ordered_hes = OrderedDict(sorted(lmao.items(), key = lambda item: item[1],reverse = False))
    action_keys = list(ordered_hes.keys())    
    if(action_keys[0] == 1):
        move_up(estado_inicial)
##        countup +=1
##        if(countup % randint(1,4) == 0 or countup == 5):
##            punishup = 1
##            countup = 0
##        else:
##            punishup = 0
        #punishdown = randint(1,2)
    elif(action_keys[0] == 2):
        move_down(estado_inicial)
##        countdown +=1
##        if(countdown % randint(1,4) == 0 or countdown == 5):
##            punishdown = 1
##            countdown = 0
##        else:
##            punishdown = 0
        
        
    elif(action_keys[0] == 3):
        move_right(estado_inicial)
##        countright +=1
##        if(countright % randint(1,4) == 0 or countright == 5):
##            punishright = 1
##            countdown = 0
##        else:
##            punishright = 0
        
        #punishleft = randint(1,2)
    elif(action_keys[0] == 4):
        move_left(estado_inicial)
        #punishleft = 1
##        countleft +=1
##        if(countleft % randint(1,4) == 0 or countleft == 5):
##            punishleft = 1
##            countdown = 0
##        else:
##            punishleft = 0
        
    print(ordered_hes)
