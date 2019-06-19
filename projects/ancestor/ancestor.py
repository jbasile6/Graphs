# what was the plan
    # do BFS from start node to each other node
    # store the path length and the earliest ancestor node
    # if path is longer or path is same length and node is smaller
    # return longest path

# solution from after hours, still need to study this

# class Stack():
#     def __init__(self):
#         self.stack = deque()
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#     def size(self):
#         return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        graph.add_edge(pair[1], pair[0])

    max_path_len = 1
    earliest_ancestor = -1

    q = Queue()
    q.enqueue([starting_node])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if (len(path) == max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))







    # graph = dict()
    # for tpl in ancestors:
    #     if tpl[1] not in graph:
    #         graph[tpl[1]].add(tpl[0])

    # def dfs(starting_vertex):
    #     nonlocal graph
    #     if starting_vertex not in graph:
    #         return -1

    #     distances = dict()

    #     visited = set()
    #     stack = Stack()
    #     stack.push([starting_vertex])
    #     while stack.size() > 0:
    #         path = stack.pop()
    #         vert = path[-1] # last element in the array stores the path
    #         if vert not in visited:
    #             for neighbor in graph[vert]:
    #                 path_new = path.copy()
    #                 path_new.append(neighbor)
    #                 stack.push(path_new)
    #                 if neighbor not in graph:
    #                     distances[neighbor] = len(path_new)
    #                     continue
    #             visited.add(vert)
        
    #     results = []
    #     max_length = -1
    #     for k, v in distances.items(): #finding max length
    #         if v > max_length:
    #             max_length = v
    #     for k, v in distances.items():
    #         if v == max_length:
    #             results.append(k)

    #     return min(results)

    # return dfs(starting_node)


