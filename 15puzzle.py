import sys
from pprint import pprint
def fifteenpuzzle(start,end):
    frontier = [[heuristica_manhattan(start), start]] 
    recorridos = []
    nodos_recorridos=0
    while frontier:
        i = 0
        for j in range(1, len(frontier)):
            if frontier[i][0] > frontier[j][0]:
                i = j
        path = frontier[i]
        frontier = frontier[:i] + frontier[i+1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in recorridos: continue
        for k in moves(endnode):
            if k in recorridos: continue
            newpath = [path[0] + heuristica_manhattan(k) - heuristica_manhattan(endnode)] + path[1:] + [k] 
            frontier.append(newpath)
            recorridos.append(endnode)
        nodos_recorridos += 1 
    print ("cantida de nodos visitados:{}".format(nodos_recorridos))
    pprint ("caminos explorados: {}".format(path))
    


def moves(estado): 
    
    posibles_movidas = []  

    subestado = eval(estado)   
    i = 0
    while 0 not in subestado[i]: i += 1
    j = subestado[i].index(0); 
    
    #moverse hacia arriba
    if i > 0:                                   
      subestado[i][j], subestado[i-1][j] = subestado[i-1][j], subestado[i][j];  
      posibles_movidas.append(str(subestado))
      subestado[i][j], subestado[i-1][j] = subestado[i-1][j], subestado[i][j]; 
    #moverse hacia abajo
    if i < 3:                                   
      subestado[i][j], subestado[i+1][j] = subestado[i+1][j], subestado[i][j]   
      posibles_movidas.append(str(subestado))
      subestado[i][j], subestado[i+1][j] = subestado[i+1][j], subestado[i][j]
    #moverse hacia la izquierda
    if j > 0:                                                      
      subestado[i][j], subestado[i][j-1] = subestado[i][j-1], subestado[i][j]   
      posibles_movidas.append(str(subestado))
      subestado[i][j], subestado[i][j-1] = subestado[i][j-1], subestado[i][j]
    #moverse hacia la derecha
    if j < 3:                                   
      subestado[i][j], subestado[i][j+1] = subestado[i][j+1], subestado[i][j]   
      posibles_movidas.append(str(subestado))
      subestado[i][j], subestado[i][j+1] = subestado[i][j+1], subestado[i][j]

    return posibles_movidas

def heuristica_manhattan(estado):
    
    distance = 0
    m = eval(estado)          
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0: continue
            distance += abs(i - (m[i][j]/4)) + abs(j -  (m[i][j]%4));
    return distance

def main():
    entrada = sys.argv[1]
    #entrada = "F21C856B49A73ED."
    L = list(entrada)
    estado_inicial_array = [0 if x=="." else int(x,16) for x in entrada]
    estado_inicial = [estado_inicial_array[0:4],estado_inicial_array[4:8],estado_inicial_array[8:12],estado_inicial_array[12:16]]
    goal_state = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    puzzle = str(estado_inicial)
    end = str(goal_state)
    fifteenpuzzle(puzzle,end)
main()
