from util import Search  # DFS/BFS algoritmus osztály
from visualize import show_menu, visualize_stepwise  # menü és vizualizációs függvények

maze = [                                   # labirintus szövegesen
    list(" # # ###  #B"),
    list(" # #   # ## "),
    list("   # #   ## "),
    list("# ## # # ## "),
    list("#    # #    "),
    list("### ## #####"),
    list("A   ##      ")
]


start = goal = None    # kezdő és célmező koordináták
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] == 'A':
            start = (y, x)
        elif maze[y][x] == 'B':
            goal = (y, x)


chosen = show_menu()                       # felhasználó választ: DFS vagy BFS

search = Search(start, goal, maze)         # kereső objektum létrehozása
if chosen == "dfs":
    path = search.depth_first_search()
else:
    path = search.breadth_first_search()


visited = search.visited_order             # bejárt mezők listája (vizualizációhoz)
visualize_stepwise(maze, visited, path, start, goal)  # lépésenkénti megjelenítés