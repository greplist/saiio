from numpy import *


class ResourceAllocationSolver(object):
  def __init__(self, f):
    self.f = f
    self.n, self.c = f.shape

    self.B = zeros([self.n, self.c])
    self.B[0] = self.f[0]

    self.x_0 = zeros([self.n, self.c])
    self.x_0[0] = range(self.c)

    self.x = []

  def generate_x(self, n, c):
    n, c = int(n), int(c)

    x_0 = self.x_0[n][c]
    if (n > 0):
      self.generate_x(n - 1, c - x_0)
    self.x.append(x_0)

  def solve(self):
    for k in xrange(1, self.n):
      for y in xrange(self.c):
        z_max, maximum = 0, -inf
        for z in xrange(y + 1):
          curr = self.f[k][z] + self.B[k - 1][y-z]
          if curr > maximum:
            z_max, maximum = z, curr

        self.x_0[k][y], self.B[k][y] = z_max, maximum

    self.generate_x(self.n - 1, self.c - 1)
    return self


if __name__ == '__main__':
  f = array([
    array([0, 3, 4, 5, 8, 9, 10]),
    array([0, 2, 3, 7, 9, 12, 13]),
    array([0, 1, 2, 6, 11, 11 ,13])
  ])
  ololo = ResourceAllocationSolver(f).solve()
  print ololo.B
  print ololo.x_0
  print ololo.x
