"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()

        que = Queue()

        que.enqueue(starting_vertex)
        
        while que.size() > 0:
            # dequeue first vert
            vert = que.dequeue()
            # if not visited
            if vert not in visited:
                # add to visited
                visited.add(vert)
                print(vert)
                # add neighbors to the queue
                for x in self.vertices[vert]:
                    que.enqueue(x)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()

        stack = Stack()
        stack.push(starting_vertex)

        while stack.size() > 0:
            vert = stack.pop()

            if vert not in visited:
                visited.add(vert)
                print(vert)

                for x in self.vertices[vert]:
                    stack.push(x)

    #create helper for dft_recursive
    def dft_recur_help(self, current, visited):
        if current.size == 0:
            return
        else:
            vert = current.pop()
            if vert not in visited:
                visited.add(vert)
                print(vert)
                for x in self.vertices[vert]:
                    current.push(x)
                self.dft_recur_help(current, visited)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        visited = set()
        stack = Stack()

        stack.push(starting_vertex)
        self.dft_recur_help(stack, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        que = Queue()
        que.enqueue([starting_vertex])
        while que.size() > 0:
            current = que.dequeue()
            if current[len(current) - 1] == destination_vertex:
                return current
            else:
                vert = current[len(current) - 1]
                visited.add(vert)

                for x in self.vertices[vert]:
                    path = current.copy()
                    path.append(x)
                    que.enqueue(path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = Stack()
        stack.push([starting_vertex])
        while stack.size() > 0:
            current = stack.pop()
            if current[len(current) - 1] == destination_vertex:
                return current
            else:
                vert = current[len(current) - 1]
                visited.add(vert)
                for x in self.vertices[vert]:
                    path = current.copy()
                    path.append(x)
                    stack.push(path)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print("VERTICES^^^^^^^^^^^")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("DFT PATH^^^^^^^^^^^^^^^^^")

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("BFT PATH^^^^^^^^^^^^^^^^^^^^")

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)
    print("DFT RECURSIVE^^^^^^^^^^^^^^^^^^^^^")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    print("BFS PATH^^^^^^^^^^^^^^^^^^^^^^^^^")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print("DFS PATH^^^^^^^^^^^^^^^^^^^^^^^^^^")
