import copy
from numpy import inf, isinf, zeros


def print_matrix(name, M):
    print(name)
    for column in M:
        print(column)


class FloydSolver(object):
  def __init__(self, g):
    self.D = copy.deepcopy(g)
    self.n = len(g[0])
    self.R = [range(self.n) for _ in range(self.n)]

  def solve(self):
    for k in xrange(self.n):
      for i in xrange(self.n):
        for j in xrange(self.n):
          if (self.D[i][k] < inf and self.D[k][j] < inf):
            distance = self.D[i][k] + self.D[k][j]
            if self.D[i][j] > distance:
              self.D[i][j] = distance
              self.R[i][j] = self.R[i][k]
    return self


if __name__=='__main__':
  g = [
      [0, 9, inf, 3, inf, inf ,inf ,inf],
      [9, 0, 2, inf, 7, inf, inf, inf],
      [inf, 2, 0, 2, 4, 8, 6, inf],
      [3, inf, 2, 0, inf, inf, 5, inf],
      [inf, 7, 4, inf, 0, 10, inf, inf],
      [inf, inf, 8, inf, 10, 0, 7, inf],
      [inf, inf, 6, 5, inf, 7, 0, inf],
      [inf, inf, inf, inf, 9, 12, 10, 0]
    ]
  res = FloydSolver(g).solve()
  print_matrix("D:", res.D)
  print_matrix("R:", res.R)
