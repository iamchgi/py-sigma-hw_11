"""

Завдання_4.
Розробити граф Вашого найпопулярнішого переміщення містом з альтернативами маршрутів,
де вузли – реперні точки, наприклад головні перехрестя, а дуги – відстані + час подолання відстані
(пропорційно до завантаження трафіка руху).
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

"""


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

    def get_adjacent_and_weight(self):
        for i in self.adjacent.keys():
            print(f"{i.id} <-> {self.adjacent[i]}")


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

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


# Рекурсивний метод пошуку оптимального шляху
def find_way(visited, weight) -> None:
    """
    :param visited: Ім'я вузлів яки вже пройшли в гілці пошуку
    :param weight: Просумований час проходження крізь ці вузли
    :return:
    """
    global best_way, best_weight, CEL
    start_vertex = graph.get_vertex(visited[len(visited) - 1])
    for vertex in start_vertex.get_connections():
        current_visited = visited.copy()
        current_weight = weight
        if vertex.get_id() not in visited:
            current_visited.append(vertex.get_id())
            current_weight += start_vertex.get_weight(vertex)
            if vertex.get_id() == CEL:
                print(current_visited, current_weight)
                if (best_weight > current_weight) or len(best_way) == 0:
                    best_weight = current_weight
                    best_way = current_visited
                continue
            find_way(current_visited, current_weight)
    return None


def init_graph() -> Graph:
    # Формування графа
    g = Graph()
    g.add_vertex('atp')
    g.add_vertex('victory')
    g.add_vertex('carina')
    g.add_vertex('home')
    g.add_vertex('sobor')
    g.add_vertex('cel')
    g.add_vertex('gaga')

    g.add_edge('gaga', 'atp', 25)
    g.add_edge('gaga', 'home', 25)
    g.add_edge('gaga', 'victory', 20)
    g.add_edge('gaga', 'sobor', 10)
    g.add_edge('atp', 'victory', 30)
    g.add_edge('atp', 'sobor', 45)
    g.add_edge('atp', 'carina', 40)
    g.add_edge('atp', 'cel', 25)
    g.add_edge('carina', 'home', 15)
    g.add_edge('sobor', 'home', 45)
    g.add_edge('victory', 'home', 15)
    return g


def graph_research_main() -> None:
    global best_way, best_weight, CEL, graph
    graph = init_graph()
    best_way = []
    best_weight = 0
    CEL = 'cel'

    print(" Відображення ребер графа")
    for v in graph:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

    print(" Відображення взаємозв'язків вершин графа")
    for v in graph:
        print('g.vert_dict[%s]=%s' % (v.get_id(), graph.vert_dict[v.get_id()]))

    print(" Розрахунок загальної довжини ребер графа")
    length_of_graph_edges = 0
    for v in graph:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            length_of_graph_edges = length_of_graph_edges + float(v.get_weight(w))
            print('length of graph edges =', length_of_graph_edges)

    print("------ Беремо вузлик графа і бачемо його сусідів ------")
    vert = graph.get_vertex('gaga')
    print(vert)
    print(f"--Від `{vert.id}` відстань до сусідів---------")
    vert.get_adjacent_and_weight()
    print("----- Дивимся сусідів його сусідів ))) -----------")
    for c in vert.get_connections():
        print(c)

    print("---Яким шляхом рушимо?----------------------------")
    find_way(['home'], 0)
    print(f"Оптимальний шлях:\n {best_way}\nОптимальний час: {best_weight}")


if __name__ == '__main__':
    graph_research_main()

''' 
РЕЗУЛЬТАТ

 Відображення ребер графа
( atp , gaga,  25)
( atp , victory,  30)
( atp , sobor,  45)
( atp , carina,  40)
( atp , cel,  25)
( victory , gaga,  20)
( victory , atp,  30)
( victory , home,  15)
( carina , atp,  40)
( carina , home,  15)
( home , gaga,  25)
( home , carina,  15)
( home , sobor,  45)
( home , victory,  15)
( sobor , gaga,  10)
( sobor , atp,  45)
( sobor , home,  45)
( cel , atp,  25)
( gaga , atp,  25)
( gaga , home,  25)
( gaga , victory,  20)
( gaga , sobor,  10)
 Відображення взаємозв'язків вершин графа
g.vert_dict[atp]=atp adjacent: ['gaga', 'victory', 'sobor', 'carina', 'cel']
g.vert_dict[victory]=victory adjacent: ['gaga', 'atp', 'home']
g.vert_dict[carina]=carina adjacent: ['atp', 'home']
g.vert_dict[home]=home adjacent: ['gaga', 'carina', 'sobor', 'victory']
g.vert_dict[sobor]=sobor adjacent: ['gaga', 'atp', 'home']
g.vert_dict[cel]=cel adjacent: ['atp']
g.vert_dict[gaga]=gaga adjacent: ['atp', 'home', 'victory', 'sobor']
 Розрахунок загальної довжини ребер графа
length of graph edges = 25.0
length of graph edges = 55.0
length of graph edges = 100.0
length of graph edges = 140.0
length of graph edges = 165.0
length of graph edges = 185.0
length of graph edges = 215.0
length of graph edges = 230.0
length of graph edges = 270.0
length of graph edges = 285.0
length of graph edges = 310.0
length of graph edges = 325.0
length of graph edges = 370.0
length of graph edges = 385.0
length of graph edges = 395.0
length of graph edges = 440.0
length of graph edges = 485.0
length of graph edges = 510.0
length of graph edges = 535.0
length of graph edges = 560.0
length of graph edges = 580.0
length of graph edges = 590.0
------ Беремо вузлик графа і бачемо його сусідів ------
gaga adjacent: ['atp', 'home', 'victory', 'sobor']
--Від `gaga` відстань до сусідів---------
atp <-> 25
home <-> 25
victory <-> 20
sobor <-> 10
----- Дивимся сусідів його сусідів ))) -----------
atp adjacent: ['gaga', 'victory', 'sobor', 'carina', 'cel']
home adjacent: ['gaga', 'carina', 'sobor', 'victory']
victory adjacent: ['gaga', 'atp', 'home']
sobor adjacent: ['gaga', 'atp', 'home']
---Яким шляхом рушимо?----------------------------
['home', 'gaga', 'atp', 'cel'] 75
['home', 'gaga', 'victory', 'atp', 'cel'] 100
['home', 'gaga', 'sobor', 'atp', 'cel'] 105
['home', 'carina', 'atp', 'cel'] 80
['home', 'sobor', 'gaga', 'atp', 'cel'] 105
['home', 'sobor', 'gaga', 'victory', 'atp', 'cel'] 130
['home', 'sobor', 'atp', 'cel'] 115
['home', 'victory', 'gaga', 'atp', 'cel'] 85
['home', 'victory', 'gaga', 'sobor', 'atp', 'cel'] 115
['home', 'victory', 'atp', 'cel'] 70
Оптимальний шлях:
 ['home', 'victory', 'atp', 'cel']
Оптимальний час: 70


'''
