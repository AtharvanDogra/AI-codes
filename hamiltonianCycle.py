path = []
visited = [False]*7
adjacent = {0:[3,4,5],1:[2,4,5],2:[1,4,6],3:[0,4,6],
            4:[0,1,2,3],5:[0,1],6:[2,3]}
start = 0
visited[start]=True
path.append(start)

def hamCycle(path, v):
    if len(path)==len(visited):
        return True
    for av in adjacent[v]:
        if not visited[av]:
            visited[av]=True
            path.append(av)
            if hamCycle(path,av):
                return True
            visited[av] = False
            path.remove(av)
    return False

hamCycle(path,start)
print(path)
                
