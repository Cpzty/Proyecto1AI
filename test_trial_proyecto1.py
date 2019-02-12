Entrada = ".4.13.4.1..4.21."
L = list(Entrada)
sudoku = [0 if x=="." else int(x)for x in Entrada]
nodes = [[]]
frontier = [[]]
values_present = [[]]
cleaner = []
current_node = 0
possible_values = [1,2,3,4]
for i in range(4):
    #filas
    nodes[0].append(sudoku[i])
    #columnas
    if(i !=0):
        nodes[0].append(sudoku[i*4])
    #cuadro adyacente    
nodes[0].append(sudoku[5])

#frontera
for value in nodes[0]:
    if value not in values_present[0] and value != 0:
        values_present[0].append(value)
print(sudoku)
print(nodes)        
#numeros disponibles
frontier[0].append((set(possible_values)-set(values_present[0])).pop())
print(frontier[0])


