entrada = "F21C856B49A73ED."
L = list(entrada)
#print(L)
estado_inicial_array = [0 if x=="." else int(x,16) for x in entrada]
from copy import deepcopy
estado_inicial = [estado_inicial_array[0:4],estado_inicial_array[4:8],estado_inicial_array[8:12],estado_inicial_array[12:16]]
move_up = deepcopy(estado_inicial)
move_down = deepcopy(estado_inicial)
y1_and_x1 = []
for x in range(4):
        for y in range(4):
            if(move_up[y][x] == 0):
                y1_and_x1 = [y,x]

columna_puntero = y1_and_x1[0]
fila_puntero = y1_and_x1[1]

move_up[columna_puntero][fila_puntero], move_up[columna_puntero-1][fila_puntero] = move_up[columna_puntero-1][fila_puntero], move_up[columna_puntero][fila_puntero]
print(estado_inicial)
print(move_up)
print(move_down)

heuristica = 0
for i in range(4):
    for j in range(4):
        value = move_up[i][j]
        if(value != 0):
            targetX = (value - 1) / 4
            targetY = (value - 1) % 4
            dx = i - targetX
            dy = j - targetY
            heuristica += abs(dx) + abs(dy) 
                #heuristica += abs(goal_state[i][j] - estado[i][j])
print("up:" + str(heuristica))
heuristica = 0
for i in range(4):
    for j in range(4):
        value = move_up[i][j]
        if(value != 0):
            targetX = (value - 1) / 4
            targetY = (value - 1) % 4
            dx = i - targetX
            dy = j - targetY
            heuristica += abs(dx) + abs(dy) 
print("down: " + str(heuristica))

   
