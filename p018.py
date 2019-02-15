import time

def increment_route(route, index=None):
    route_len = len(route)
    
    if index is None:
        for i in reversed(range(0, route_len)):
            if route[i] is False:
                route[i:] = [False] * (route_len - i)
                route[i] = True
                break
    else:
        for i in reversed(range(0, index+1)):
            if route[i] is False:
                route[i:] = [False] * (route_len - i)
                route[i] = True  
                break                 
    
# customized version of Dijkstras algorithm for this search problem / branch and bound algorithm
# there is a more efficient way of doing this (bottom-up), which I will implement for problem 67
def compute(graph_layers):
    graph_route = [False] * (len(graph_layers) - 1)
    complete_route = [True] * (len(graph_layers) - 1)
    routing_finished = False
    
    max_sum = 0

    while not routing_finished:
        if graph_route == complete_route:
            routing_finished = True
        
        current_node = graph_layers[0][0]
        accumumated_weight = current_node['weight']

        weak_route = False
        
        for i in range(len(graph_route)):
            next_node_index = current_node['descendants'][0 if not graph_route[i] else 1]
            next_node = graph_layers[i + 1][next_node_index]

            if accumumated_weight + next_node['weight'] <= next_node['max_accumulated_weight'] and graph_route[:i+1] != next_node['max_route']:
                increment_route(graph_route, index=i)
                weak_route = True
                break
            
            accumumated_weight += next_node['weight']
            next_node['max_accumulated_weight'] = accumumated_weight
            next_node['max_route'] = graph_route[:i+1]
            current_node = next_node
        
        if not weak_route:
            max_sum = accumumated_weight if accumumated_weight > max_sum else max_sum
            increment_route(graph_route)
 
    return max_sum


if __name__ == '__main__':
    graph_layers = []

    with open('p018.txt') as f:
        for line in f:
            layer_str = line.rstrip('\n').split()
            layer = list(map(int, layer_str))
            graph_layers.append(layer)
    
    # create appropriate data structure
    for i in range(len(graph_layers)):
        layer = graph_layers[i]

        for j in range(len(layer)):
            layer[j] = {
                'weight': layer[j],
                'max_accumulated_weight': 0,
                'max_route': None,
                'descendants': [j, j+1] if i != (len(graph_layers) - 1) else None
            }

    start = time.time()
    print(compute(graph_layers))
    print(time.time() - start)