Entrada = ".4.13.4.1..4.21."
L = list(Entrada)
sudoku = sudoku = [0 if x=="." else int(x)for x in Entrada]
nodes = [[]]
frontier = [[]]
current_node = 0
for i in range(4):
    #filas
    nodes[0].append(sudoku[i])
    #columnas
    if(i !=0):
        nodes[0].append(sudoku[i*4])
    #cuadro adyacente
    if(current_node<2)
nodes[0].append(sudoku[5])

for value in nodes[0]:
    if value not in frontier[0] and value != 0:
        frontier[0].append(value)

print(frontier)
