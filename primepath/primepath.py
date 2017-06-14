# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import linecache

class PrimePath:
    @staticmethod
    def read_graph():
        graph = nx.DiGraph()  # 构造一个图
        # G.add_node(1)  #添加一个节点
        # start = 0
        # end = 6
        # graph.add_nodes_from([0, 1, 2, 3, 4, 5, 6])  # 添加一个节点列表
        # edges = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4], [3, 6], [4, 6], [4, 5], [5, 4]]  # 所有边
        # graph.add_nodes_from([0, 1, 2, 3])
        # edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 0]]
        n = 0
        file = 'case_cfg.txt'
        with open(file) as f:
            for x in f:
                n += 1
            # print n

        edges = []
        for i in range(0, n):
            next_nodes = linecache.getline(file, i + 1)
            a = next_nodes.replace(',', '')
            a = a.split(' ')
            for j in a:
                j = int(j)
                # print j
                if j == -1:
                    break
                edge = [i, j]
                # print edge
                edges.append(edge)
        for ed in edges:
            graph.add_edge(ed[0], ed[1])

        nx.draw(graph)
        plt.show()
        return graph

    def __init__(self):
        # self.start, self.end,
        self.graph = self.read_graph()
        self.prime_path_list = []

    def get_prime_path(self):
        self.breadth_first_search()
        return self.prime_path_list

    def breadth_first_search(self):
        path_list = map(lambda ele: [ele], self.graph.nodes())
        while len(path_list) > 0:
            self.prime_path_list.extend(filter(lambda ele: self.is_prime_path(ele), path_list))
            path_list = filter(lambda ele: self.is_going_expand(ele), path_list)  # 判断是否可扩展
            path_list = reduce(lambda l, r: l + r, map(lambda ele: self.expand_path(ele), path_list), [])
            if path_list:
                print ' path :', path_list

    @staticmethod
    def is_loop(path):
        return path[0] == path[-1]   # 如果首尾相同

    def is_prime_path(self, path):
        if len(path) >= 2 and self.is_loop(path):   # 双向箭头的prime path
            return True
        elif self.is_reaching_head(path) and self.is_reaching_end(path):    # 首没有被指向 尾部没有指出
            return True
        else:
            return False

    def is_reaching_head(self, path):
        expand_nodes = map(lambda edge: edge[0], self.graph.in_edges(path[0]))  # in_edges 指向path[0]的边
        for node in expand_nodes:
            if node not in path or node == path[-1]:
                return False
        return True    # 没有指向该节点的边，该节点作为head

    def is_reaching_end(self, path):
        expand_nodes = map(lambda edge: edge[1], self.graph.out_edges(path[-1]))  # 指出的边 path[-1]是列表最右的node
        for node in expand_nodes:
            if node not in path or node == path[0]:  # 如果node不在path中 或者node和初节点一样 false
                return False
        return True  # 后面没有指向的点 返回true

    def is_going_expand(self, path):
        if self.is_prime_path(path) or self.is_reaching_end(path):  # 如果是prime path或者到达底部 返回flase
            return False
        else:
            return True

    def expand_path(self, path):
        path_list = []
        expand_nodes = map(lambda edge: edge[1], self.graph.out_edges(path[-1]))
        for node in expand_nodes:
            if node not in path or node == path[0]:
                path_list.append(path + [node])
        return path_list


if __name__ == '__main__':
    new_file = 'E:\\case_cfg.txt'
    f = open(new_file, 'w')
    b = PrimePath().get_prime_path()
    b = sorted(b, key=lambda d: (len(d), d))
    # print b
    a = 'prime path list:' + str(b)
    print a
    c = int(len(b))
    print c
    f.writelines(str(len(b)) + '\n')
    for j in range(c):
        f.writelines(str(b[j]) + '\n')
