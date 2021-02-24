STACK s
visited = []
DFS(v)
    push(s, v)
    while not isEmpty (s):
        v = pop(s)
        if not visited[v]
            visit(v)
            for each w in adjacency(v)
                if not visited[w]
                    push(s,w)
