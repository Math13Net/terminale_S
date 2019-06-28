def dijkstra(graph,position,dest,visited=[],distances={},predecessors={}):
    
    # On verifie si les 2 points sont dans notre réseau
    if position not in graph:
        print('Le point de départ n\'existe pas.')
    if dest not in graph:
        print('Le point d\'arrivé n\'existe pas.')    
    
    if position != dest:
        # On commence en mettant le point de départ à 0
        if not visited: 
            distances[position]=0
        # Puis nous visitons les points voisins pour calculer leurs distances 
        for neighbor in graph[position] :
            if neighbor not in visited:
                new_distance = distances[position] + graph[position][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = position
        # On marque les points voisins comme étant visités
        visited.append(position)
        # Maintenant que les points voisins sont visités, on choisit le prochain point avec le poids le plus bas.

        unvisited={}   
        for p in graph:
            if p not in visited:
                unvisited[p] = distances.get(p,float('inf'))        
        dijkstra(graph,min(unvisited, key=unvisited.get),dest,visited,distances,predecessors)
    else :
        # Maintenant que tous les points dans le réseau sont visités, on obtient le chemin 
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('Le chemin le plus court (reste a mettre a l\'envers) : '+str(path)+" avec une distance de "+str(distances[dest]))


    
start = input('Point de départ : ').lower()
dest = input ('Point d\'arrivé : ').lower()
# Le réseau est donné sous la forme de "graph"
graph = {'a':{'b':2,'c':5},'b':{'e':2},'c':{'e':1,'b':2},'d':{'c':4,'b':1},'e':{'f':2,'d':4},'f':{'d':1}}
dijkstra(graph,start,dest)
