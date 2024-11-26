
'''

Завдання_4.
Розробити граф Вашого найпопулярнішого переміщення містом з альтернативами маршрутів,
де вузли – реперні точки, наприклад головні перехрестя, а дуги – відстані + час подолання відстані
(пропорційно до завантаженню трафіка руху).
Розробити програмний скрипт обчислення оптимального маршруту за мінімумом суми значень дуг графа (відстань+час).


Приклад реалізація графа з python:

Особливість - наявна довжина ребер графа.

Створити структуру даних graphs - означає встановити елементи та зв'язки між ними:

Дії над графом:
Формування графа;
Відображення вершин;
Відображення ребер графа;
Додати / видалити вузол графа;
Знайти вузол графа.

https://www.bogotobogo.com/python/python_graph_data_structures.php

'''



class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

if __name__ == '__main__':

    # Формування графа

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)



    # Відображення ребер графа
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

    # Відображення взаємозвязку вершин графа
    for v in g:
        print('g.vert_dict[%s]=%s' % (v.get_id(), g.vert_dict[v.get_id()]))

    # Розрахунок загальної довжини ребер графа
    length_of_graph_edges = 0
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            length_of_graph_edges = length_of_graph_edges + float(v.get_weight(w))
            print('length of graph edges =', length_of_graph_edges)

