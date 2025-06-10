class Node:
    def __init__(self, state, parent, action):
        self.state = state      # x, y
        self.parent = parent    # ahonnan jöttünk
        self.action = action    # elvégzett lépés


class StackFrontier:
    def __init__(self):
        self.frontier = [] # stack - verem
    
    # csomópont hozzáadása
    def add(self, node):
        self.frontier.append(node)
    
    # üres-e a stack
    def empty(self):
        return len(self.frontier) == 0

    # elem kivétele
    def remove(self):
        if self.empty():
            raise Exception("Üres a stack!")
        else:
            node = self.frontier[-1] # utolsó elemet kérjük LIFO elv alapján
            self.frontier = self.frontier[:-1] # minden elem kivéve az utolsó
            return node
    
    # állapot tartalmaz?
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
        #for state in self.frontier:
        #    if node.state == state:
        #        return True

        

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Üres a sor")
        else:
            node = self.frontier[0] # FIFO elv alapján, első elem
            self.frontier = self.frontier[1:] # az első elem után minden
            return node
        

class Search:
    def __init__(self, start, goal, maze):
        self.start_node = Node(state=start, parent=None, action=None)
        self.goal = goal
        self.maze = maze
        self.visited_order = [] # csomópontok sorrendje, bejárt


    def get_neighbors(self, state):
        y, x = state 
        neighbors = []
        for (dy, dx), action in [((1,0), "down"), ((0,1), "right"), ((0,-1), "left"), ((-1,0), "up")]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(self.maze) and 0 <= nx < len(self.maze[0]):
                if self.maze[ny][nx] != '#':
                    neighbor_state = (ny, nx)
                    neighbors.append((neighbor_state, action)) 
        return neighbors


    
    def depth_first_search(self):
        frontier = StackFrontier()
        frontier.add(self.start_node) # kezdeti csomópont
        explored = set() # halmaz, amiket bejártunk mezők

        while not frontier.empty(): # amíg nem üres
            node = frontier.remove() # kiveszek egy csomópontot

            self.visited_order.append(node.state) # vizualizációhoz, ahol voltunk elmentjük

            # ha elértük célt
            if node.state == self.goal:
                path = []
                while node.parent is not None: # amíg visszakövethető
                    path.append(node.state)
                    node = node.parent  # szülőn keresztül haladunk
                path.reverse()
                return path # útvonalat visszaadjuk
            
            # más esetben -> tehát nem cél
            explored.add(node.state)
            # lekérem az összes szomszédot
            neighbors = self.get_neighbors(node.state) # listát ad vissza, amely tuplet tartalmaz
            # => [(y,x), (y,x)...]

            # megvizsgáljuk az összes szomszédot
            for n_state, action in neighbors:
                # ha még nincs a "várólistán", és még nem jártunk ott (set)
                if not frontier.contains_state(n_state) and n_state not in explored:
                    child = Node(state=n_state, parent=node, action=action)
                    frontier.add(child)
        
        return None # Ha nincs megoldás
    

    def breadth_first_search(self):
        """
        HÁZI! 
        HINT: NAGYON hasonló az előzőhöz (DFS)
        BFS algoritmus implementációja
        Használjuk fel a már meglévő Node, QueueFrontier osztályt
        """
        pass
