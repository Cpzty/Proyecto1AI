import sys
import numpy as np
#entrada = sys.argv[1]
entrada = "F21C856B49A73ED."
L = list(entrada)
#print(L)
estado_inicial_array = [0 if x=="." else int(x,16) for x in entrada]
estado_inicial = np.matrix([estado_inicial_array[0:4],estado_inicial_array[4:8],estado_inicial_array[8:12],estado_inicial_array[12:16]])
print(estado_inicial)
fila_puntero = 0
columna_puntero = 0

def calculo_heuristica(estado):
    heuristica = 0
    counter = 1
    for i in range(4):
        for j in range(4):
            if(estado.item(i,j) != counter):
                heuristica +=1
            counter +=1
    return heuristica

        
#huehue = calculo_heuristica(estado_inicial)
#print(huehue)
def find_empty_space(estado):
    for x in range(4):
        for y in range(4):
            if(estado.item(y,x) == 0):
                y_and_x = [y,x]
    return y_and_x

def move_up(estado):
    global fila_puntero,columna_puntero
    fila_posicionfila = find_empty_space(estado_inicial)
    fila_puntero = fila_posicionfila[1]
    columna_puntero = fila_posicionfila[0]
    if(columna_puntero !=0):
        estado[columna_puntero,fila_puntero], estado[columna_puntero-1,fila_puntero] = estado[columna_puntero-1,fila_puntero], estado[columna_puntero,fila_puntero]
    return estado

def move_down(estado):
    global fila_puntero,columna_puntero
    fila_posicionfila = find_empty_space(estado_inicial)
    fila_puntero = fila_posicionfila[1]
    columna_puntero = fila_posicionfila[0]
    if(columna_puntero !=3):
        estado[columna_puntero,fila_puntero], estado[columna_puntero+1,fila_puntero] = estado[columna_puntero+1,fila_puntero], estado[columna_puntero,fila_puntero]
    return estado

def move_right(estado):
    global fila_puntero,columna_puntero
    fila_posicionfila = find_empty_space(estado_inicial)
    fila_puntero = fila_posicionfila[1]
    columna_puntero = fila_posicionfila[0]
    if(fila_puntero !=3):
        estado[columna_puntero,fila_puntero], estado[columna_puntero,fila_puntero+1] = estado[columna_puntero,fila_puntero+1], estado[columna_puntero,fila_puntero]
    return estado

def move_left(estado):
    global fila_puntero,columna_puntero
    fila_posicionfila = find_empty_space(estado_inicial)
    fila_puntero = fila_posicionfila[1]
    columna_puntero = fila_posicionfila[0]
    if(fila_puntero !=0):
        estado[columna_puntero,fila_puntero], estado[columna_puntero,fila_puntero-1] = estado[columna_puntero,fila_puntero-1], estado[columna_puntero,fila_puntero]
    return estado
    



