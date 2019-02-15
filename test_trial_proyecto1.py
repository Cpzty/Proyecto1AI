#variables globales
Entrada = ""
Entrada = ".4.13.4.1..4.21."
L = list(Entrada)
sudoku = [0 if x=="." else int(x)for x in Entrada]

frontier = [[]]
values_present = [[]]
cleaner = []
current_node = 0
possible_values = [1,2,3,4]
#for i in range(4):
    #filas
   # nodes[0].append(sudoku[i])
    #columnas
  #  if(i !=0):
 #       nodes[0].append(sudoku[i*4])
    #cuadro adyacente    
#nodes[0].append(sudoku[5])


#rows
row1 = []
row2 = []
row3 = []
row4 = []
row1 = sudoku[0:4]
row2 = sudoku[4:8]
row3 = sudoku[8:12]
row4 = sudoku[12:16]
#cols
col1 = []
col2 = []
col3 = []
col4 = []
column_traverse = 0

for i in range(4):
    col1 = col1 + sudoku[column_traverse:column_traverse+1]
    col2 = col2 + sudoku[column_traverse+1:column_traverse+2]
    col3 = col3 + sudoku[column_traverse+2:column_traverse+3]
    col4 = col4 + sudoku[column_traverse+3:column_traverse+4]
    column_traverse += 4

#nodos
#si hago un append normal tengo que usar un contador que corra la posicion inicial para que inicie sobre el cuadro del nodo.
node1 =  []
node2 =  []
node3 =  []
node4 =  []
node5 =  []
node6 =  []
node7 =  []
node8 =  []
node9 =  []
node10 = []
node11 = []
node12 = []
node13 = []
node14 = []
node15 = []
node16 = []

def create_update_nodes():
    global node1,node2,node3,node4,node5,node6,node7,node8,node9,node10,node11,node12,node13,node14,node15,node16
    
    node1.append(row1 + col1[1:] + col2[1:2])
    node2.append(row1 + col2[1:] + col1[1:2])
    node3.append(row1 + col3[1:] + col4[1:2])
    node4.append(row1 + col4[1:] + col3[1:2])
    #el skip no se ve muy bien pero se ordena de la manera mas facil de asegurarse que estan todos los numeros
    node5.append(row2 + col1[0:1] + col1[2:] + row1[1:2])
    node6.append(row2 + col2[0:1] + col2[2:] + row1[0:1])
    node7.append(row2 + col3[0:1] + col3[2:] + col4[0:1])
    node8.append(row2 + col4[0:1] + col4[2:] + col3[0:1])
    #3er fila
    node9.append( row3 + col1[0:2] + col1[3:] + row4[1:2])
    node10.append(row3 + col2[0:2] + col2[3:] + row4[0:1])
    node11.append(row3 + col3[0:2] + col3[3:] + row4[3:4])
    node12.append(row3 + col4[0:2] + col4[3:] + row4[2:3])
    #4a fila
    #ya no hay skip como la primera fila
    node13.append(row4 + col1[:3] + row3[1:2])
    node14.append(row4 + col2[:3] + row3[0:1])
    node15.append(row4 + col3[:3] + row3[3:4])
    node16.append(row4 + col4[:3] + row3[2:3])
    
create_update_nodes()

#frontera

for i in range(1,17):
    print("node"+ str(i))
for value in nodes[0]:
    if value not in values_present[0] and value != 0:
        values_present[0].append(value)
print(sudoku)
print(nodes)        
#numeros disponibles
frontier[0].append((set(possible_values)-set(values_present[0])).pop())
print(frontier[0])


