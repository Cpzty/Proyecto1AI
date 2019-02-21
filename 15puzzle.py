import sys
from pprint import pprint

def heuristica_manhattan(estado):
    heuristica = 0
    m = eval(estado)          
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0:
                continue
            heuristica += abs(i - (m[i][j]/4)) + abs(j -  (m[i][j]%4));
    return heuristica


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

def moves_reverse(estado): 
    
    posibles_movidas = []  

    subestado = eval(estado)   
    i = 0
    while 0 not in subestado[i]: i += 1
    j = subestado[i].index(0); 

    #moverse hacia la derecha
    if j < 3:                                   
      subestado[i][j], subestado[i][j+1] = subestado[i][j+1], subestado[i][j]   
      posibles_movidas.append(str(subestado))
      subestado[i][j], subestado[i][j+1] = subestado[i][j+1], subestado[i][j]

    #moverse hacia abajo
    if i < 3:                                   
      subestado[i][j], subestado[i+1][j] = subestado[i+1][j], subestado[i][j]   
      posibles_movidas.append(str(subestado))
      subestado[i][j], subestado[i+1][j] = subestado[i+1][j], subestado[i][j]
    #moverse hacia arriba
    if i > 0:                                   
      subestado[i][j], subestado[i-1][j] = subestado[i-1][j], subestado[i][j];  
      posibles_movidas.append(str(subestado))
      subestado[i][j], subestado[i-1][j] = subestado[i-1][j], subestado[i][j]; 
    #moverse hacia la izquierda
    if j > 0:                                                      
      subestado[i][j], subestado[i][j-1] = subestado[i][j-1], subestado[i][j]   
      posibles_movidas.append(str(subestado))
      subestado[i][j], subestado[i][j-1] = subestado[i][j-1], subestado[i][j]

    return posibles_movidas

def fifteenpuzzle_reverse(start,end):
    #frontera posee la heuristica y el estado
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
        #print(endnode)
        if endnode == end:
            break
        if endnode in recorridos:
            continue
        for k in moves_reverse(endnode):
            if k in recorridos:
                continue
            newpath = [path[0] + heuristica_manhattan(k) - heuristica_manhattan(endnode)] + path[1:] + [k] 
            frontier.append(newpath)
            recorridos.append(endnode)
        nodos_recorridos += 1
    if(nodos_recorridos == 10000):
        print("es probable que este puzzle no tenga solucion")
        print ("se visitaron :{} nodos".format(nodos_recorridos))
    else:
        print ("cantida de nodos visitados:{}".format(nodos_recorridos))
        pprint ("caminos explorados: {}".format(path))



def fifteenpuzzle(start,end):
    #frontera posee la heuristica y el estado
    frontier = [[heuristica_manhattan(start), start]] 
    recorridos = []
    nodos_recorridos=0
    while frontier and nodos_recorridos<20000:
        i = 0
        for j in range(1, len(frontier)):
            if frontier[i][0] > frontier[j][0]:
                i = j
        path = frontier[i]
        frontier = frontier[:i] + frontier[i+1:]
        endnode = path[-1]
        #print(endnode)
        if endnode == end:
            break
        if endnode in recorridos:
            continue
        for k in moves(endnode):
            if k in recorridos:
                continue
            newpath = [path[0] + heuristica_manhattan(k) - heuristica_manhattan(endnode)] + path[1:] + [k] 
            frontier.append(newpath)
            recorridos.append(endnode)
        nodos_recorridos += 1
    if(nodos_recorridos == 20000):
        print("es probable que este puzzle no tenga solucion")
        print ("se visitaron :{} nodos".format(nodos_recorridos))
    else:
        print ("cantida de nodos visitados:{}".format(nodos_recorridos))
        pprint ("caminos explorados: {}".format(path))
    
def main():
    entrada = sys.argv[1]
    #entrada = "F21C856B49A73ED."
    L = list(entrada)
    estado_inicial_array = [0 if x=="." else int(x,16) for x in entrada]
    estado_inicial = [estado_inicial_array[0:4],estado_inicial_array[4:8],estado_inicial_array[8:12],estado_inicial_array[12:16]]
    goal_state = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    #goal_state = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    #test1 fallo
    test1 = [[5,2,3,10],[9,11,15,7],[13,4,1,12],[14,8,0,6]]
    #test2 fallo
    #test2 = [[1,0,3,4],[9,6,2,11],[13,5,10,7],[14,8,15,12]]
    #test3 = [[5,3,6,4],[2,11,8,12],[1,13,10,7],[9,0,14,15]]
    #test4 es resoluble
    test4 = [[1,2,3,4],[5,6,7,8],[0,9,10,11],[12,13,14,15]]
    puzzle = str(estado_inicial)
    end = str(goal_state)
    fifteenpuzzle(puzzle,end)

def goalstate2():
    #entrada = sys.argv[1]
    entrada = "F21C856B49A73ED."
    L = list(entrada)
    estado_inicial_array = [0 if x=="." else int(x,16) for x in entrada]
    estado_inicial = [estado_inicial_array[0:4],estado_inicial_array[4:8],estado_inicial_array[8:12],estado_inicial_array[12:16]]
    #goal_state = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    goal_state = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    #test1 fallo
    #test1 = [[5,2,3,10],[9,11,15,7],[13,4,1,12],[14,8,0,6]]
    #test2 fallo
    #test2 = [[1,0,3,4],[9,6,2,11],[13,5,10,7],[14,8,15,12]]
    #test3 = [[5,3,6,4],[2,11,8,12],[1,13,10,7],[9,0,14,15]]
    test4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,0,15]]
    puzzle = str(test4)
    end = str(goal_state)
    fifteenpuzzle_reverse(puzzle,end)


main()
#goalstate2()

