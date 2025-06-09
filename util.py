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
        for dy, dx in [(1,0), (0,1), (0,-1), (-1,0)]:  # le, jobb, bal, fel
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(self.maze) and 0 <= nx < len(self.maze[0]):  # pályán belül
                if self.maze[ny][nx] != '#':  # nem fal
                    neighbors.append((ny, nx))
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
