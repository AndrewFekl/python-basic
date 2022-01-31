def generate_permutation(point_list, M, prefix=None):
    
    M = len(point_list) if M==-1 else M
    prefix = prefix or []
    
    if M == 0:
        
        total_distance = 0
        route = f"{point1} ->"
        
        if len(prefix) != 0:
            
            distance = get_distance(point1, prefix[0])
            total_distance += distance
            route += f"{prefix[0]}[{distance}] ->"
            
        if len(prefix) >= 2:
            
            for n in range(1, len(prefix)):
                
                distance = get_distance(prefix[n], prefix[n-1])
                total_distance += distance
                route += f"{prefix[n]}[{distance}] ->"
                
        distance = get_distance(prefix[-1], point1)
        total_distance += distance
        route += f"{point1}[{distance}] = {total_distance}"
                
        routes.append((total_distance, route))
        #print(route)
        #print(prefix)
        return
    
    for point in point_list:
        if point in prefix:
            continue
        prefix.append(point)
        generate_permutation(point_list, M-1, prefix)
        prefix.pop()


def get_minimal_route(routes):

    minimal_route = routes[0]
    for i in range(1, len(routes)):
        if routes[i][0] < minimal_route[0]:
            minimal_route = routes[i]
            
    return minimal_route[1]


def get_distance(point1, point2):
    
    return ((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)**0.5


if __name__ == "__main__":
    
    point1 = (0, 2)
    point2 = (2, 5)
    point3 = (5, 2)
    point4 = (6, 6)
    point5 = (8, 3)
    point_list = [point2, point3, point4, point5]
    
    routes = []
    
    generate_permutation(point_list, -1)
    
    minimal_route = get_minimal_route(routes)
    
    print(minimal_route)
    