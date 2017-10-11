from numpy import array, inf
from ford_falkerson import *

class MinCostFlowSolver(object):

  def add_values(self, i, j, c, x):
    self.g[i].append(len(self.edges))
    self.edges.append([i, j, c, x])

  def create_graph(self, inp):
    for i, j, c, x in inp:
      self.add_values(i, j, c, x)
      self.add_values(j, i, c, -x)

  def __init__(self, inp, n, basic_indexes, nonbasic_indexes):
    self.n = n
    self.g = [[] for _ in range(n)]
    self.edges = []
    self.create_graph(inp)
    self.basic_indexes = basic_indexes
    self.nonbasic_indexes = nonbasic_indexes

  def calculate_u(self):
    self.u = [None for _ in range(self.n)]
    self.u[0] = 0
    def dfs_for_u(el):
      for index in self.g[el]:
        if index in self.basic_indexes or index^1 in self.basic_indexes:
          index = index/2 * 2
          i, j, c, x = self.edges[index]
          if self.u[i] is None and self.u[j] is None:
            continue
          if self.u[i] is None:
            self.u[i] = self.u[j] + c
            dfs_for_u(i)
          elif self.u[j] is None:
            self.u[j] = self.u[i] - c
            dfs_for_u(j)
    for item in range(self.n):
      dfs_for_u(item)


  def calculate_delta(self):
    self.delta = []
    for index in self.nonbasic_indexes:
      i, j, c, x = self.edges[index]
      self.delta.append(self.u[i] - self.u[j] - c)

  def dfs(self, i0, j0, ind0):
    for index in self.g[j0]:
      i, j, c, x = self.edges[index]
      if j == i0 and i == j0:
        continue
      if index in self.basic_indexes or index^1 in self.basic_indexes:
        if index not in self.edges_in_cycle and index^1 not in self.edges_in_cycle:
          self.edges_in_cycle.append(index)
          self.dfs(i, j, index)
          if self.finish_dfs:
            return
          self.edges_in_cycle.pop()
        else:
          self.finish_dfs = True

  def find_tetta(self):
    self.tetta = inf
    for index in self.edges_in_cycle:
      if index % 2 == 0:
        continue
      i, j, c, x = self.edges[index]
      if abs(x) < self.tetta:
        self.tetta = abs(x)
        self.index_tetta = index/2 *2

  def correct_flow(self):
    for index in self.edges_in_cycle:
      self.edges[index][3] += self.tetta
      self.edges[index^1][3] -= self.tetta

  def solve(self):
    while True:
      self.calculate_u()
      self.calculate_delta()
      if all(item <= 0 for item in self.delta):
        return self

      for i, el in enumerate(self.delta):
        if el > 0:
          index_delta = i

      ind = list(self.nonbasic_indexes)[index_delta]
      i0, j0, c0, x0 = self.edges[ind]

      self.basic_indexes.add(ind)
      self.nonbasic_indexes.remove(ind)

      self.finish_dfs = False
      self.edges_in_cycle = []
      self.dfs(i0, j0, ind)

      self.find_tetta()
      self.correct_flow()

      self.basic_indexes.remove(self.index_tetta)
      self.nonbasic_indexes.add(self.index_tetta)

  def get_x(self):
    return [x for index, [i, j, c, x] in enumerate(self.edges) if index % 2 == 0]

if __name__=="__main__":
    inp = [
      [0, 1, 1, 1],
      [1, 5, 3, 0],
      [2, 1, 3, 3],
      [2, 3, 5, 1],
      [4, 2, 4, 0],
      [4, 3, 1, 5],
      [5, 2, 3, 9],
      [5, 4, 4, 0],
      [5, 0, -2, 0]
    ]
    n = 6
    basic_indexes = set([0, 4, 6, 10, 12])
    nonbasic_indexes = set([2, 8, 14, 16])

    # res = [4, 0, 0, 0, 0, 6, 5, 1, 3]
    print MinCostFlowSolver(inp, n, basic_indexes, nonbasic_indexes).solve().get_x()
