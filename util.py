class Node:
    """
    Csomópont osztály kódja
    """
    pass


class StackFrontier:
    """
    Verem osztály kódja
    """
    pass

        

class QueueFrontier:
    """
    Sor osztály kódja
    """
    pass
        

class Search:
    pass


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
        """
        DFS algoritmus implementációja
        Használjuk fel a már meglévő Node, StackFrontier osztályt
        """
        pass
    

    def breadth_first_search(self):
        """
        BFS algoritmus implementációja
        Használjuk fel a már meglévő Node, QueueFrontier osztályt
        """
        pass
