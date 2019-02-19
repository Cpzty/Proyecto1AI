class Node():
    def __init__(self,parent=None,position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self,other):
        return self.position == other.position

def astar(maze,start,end):
    #nodo inicial y final
    start_node = Node(None,start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None,end)
    end_node.g = end_node.h = end_node.f = 0
    #lista abierta y cerrada
    open_list = []
    closed_list = []
    #agregar nodo inicial
    open_list.append(start_node)
    #Loop hasta encontrar goal state o error
    while(len(open_list) > 0):
        #sobre el nodo actual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if(item.f < current_node.f):
                current_node = item
                current_index = index
        #mover de lista abierta a cerrada
        open_list.pop(current_index)
        closed_list.append(current_node)

        #meta
        if(current_node == end_node):
            path = []
            current = current_node
            while(current is not None):
                path.append(current_position)
                current = current.parent
            #camino al revez
            return path[::-1]
        #hijos
        children = []
        for new_position in [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]:
            #posicion del nodo
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            #asegurarse que no se pase
            if node_position[0] >(len(maze)-1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1])-1) or node_position[1]<0:
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            #nuevo nodo
            new_node = Node(current_node,current_position)
            #agregar nuevo nodo a hijos
            children.append(new_node)
        #loop en los hijos
        for child in children:
            #hijos en la lista cerrada
            for closed_child in closed_list:
                if child == closed_child:
                    continue
        
