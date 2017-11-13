# -*- coding: utf-8 -*-


def dijkstra_longest_path(graph, start, p={}, u=[], d={}):
    if len(p) == 0: p[start] = 0 # инициализация начального пути
    # print "start V: %d, " % (start)
    for x in graph[start]:
        if (x not in u and x != start):
            if (x not in p.keys() or (graph[start][x] + p[start]) > p[x]):
                p[x] = graph[start][x] + p[start]

    u.append(start)

    max_v = 0
    max_x = None
    for x in p:
        # print "x: %d, p[x]: %d, mv %d" % (x, p[x], min_v)
        if (p[x] > max_v or max_v == 0) and x not in u:
                min_x = x
                min_v = p[x]

    if(len(u) < len(graph) and max_x):
        return dijkstra_longest_path(graph, max_x, p, u)
    else:
        return p


if __name__ == '__main__':
    a, b, c, d, e, f, g, h = range(8)
    N = [
        {b: 7, c: 9, f: 14},
        {a: 7, c: 10, d: 15},
        {a: 9, b: 10, d: 11, f: 2},
        {b: 15, c: 11, e: 6},
        {d: 6, f: 9},
        {a: 14, c: 2, e: 9},
        {h: 2},
        {g: 2},
    ]
    print dijkstra_longest_path(N, a)
# b in N[a] - смежность
# len(N[f]) - степень
# N[a][b] - вес (a,b)
# print N[a][b]
