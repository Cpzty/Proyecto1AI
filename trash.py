#trash
node_travel = 0

def row_check(row):
    if(row.count(0) == 1):
        visited = []
        for value in row:
        	if value not in visited and value != 0:
        		visited.append(value)
        row = [3 if x == 0 else x for x in row]
    return row

def fill_node(node,current_row):
    global node_travel
    if(node[node_travel]  == 0):
        visited = []
        for value in node:
            if value not in visited:
                visited.append(value)
        visited.remove(0)
        if(len(visited) == 3):
            #update row y node
            missingno = 10 - sum(visited)
            current_row[node_travel] = missingno
            node[node_travel] = missingno
        elif(len(visited) == 4 ):
            print("el programa no tiene solucion")
    if(node_travel <3):
        node_travel+=1
    else:
        node_travel = 0
    
    
    

    
def solve_sudoku():
    Entrada = ".4.13.4.1..4.21."
    L = list((Entrada))
    sudoku = [0 if x=="." else int(x)for x in Entrada]
    first_row = sudoku[0:4]
    second_row = sudoku[4:8]
    third_row = sudoku[8:12]
    fourth_row = sudoku[12:16]
    first_node = []
    first_node.extend(first_row + second_row[0:2] + third_row[0:1] + fourth_row[0:1])
    fill_node(first_node,first_row)
    first_row = row_check(first_row)
    #updatear el nodo por si first_row fue modificado por row_check
    first_node[0:4] = first_row
    print(first_row)
    print(first_node)
    #segundo nodo
    second_node = []
    second_node.extend(first_row + second_row[0:2] + third_row[1:2] + fourth_row[1:2])
    fill_node(second_node,first_row)
    first_row = row_check(first_row)
    first_node[0:4] = first_row
    print(second_node)
    #tercer nodo
    third_node = []
    third_node.extend(first_row + second_row[2:4] + third_row[2:3] + fourth_row[2:3])
    fill_node(third_node,first_row)
    first_row = row_check(first_row)
    first_node[0:4] = first_row
    print(third_node)
    #cuarto nodo
    fourth_node = []
    fourth_node.extend(first_row + second_row[2:4] + third_row[3:4] + fourth_row[3:4])
    fill_node(fourth_node,first_row)
    first_row = row_check(first_row)
    first_node[0:4] = first_row
    print(fourth_node)
    #quinto_nodo
    fifth_node = []
    fifth_node.extend(second_row + first_row[0:2]  + third_row[0:1] + fourth_row[0:1])
    fill_node(fifth_node,second_row)
    second_row = row_check(second_row)
    fifth_node[0:4] = second_row
    print(fifth_node)
    #sexto nodo
    sixth_node = []
    sixth_node.extend(second_row + first_row[0:2] + third_row[1:2] + fourth_row[1:2])
    fill_node(sixth_node,second_row)
    second_row = row_check(second_row)
    fifth_node[0:4] = second_row
    print(sixth_node)
    
solve_sudoku()

