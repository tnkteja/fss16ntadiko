#    Original Author : Simon Wessing
#    From : TU Dortmund University
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function,division
import sys, os
import random

sys.path.append(os.path.abspath("."))
__author__ = 'george'

def gt(a, b): return a>b

def lt(a, b): return a<b

def gte(a, b): return a>=b

def lte(a, b): return a<=b

class HyperVolume:
  """
  Hypervolume computation based on variant 3 of the algorithm in the paper:
  C. M. Fonseca, L. Paquete, and M. Lopez-Ibanez. An improved dimension-sweep
  algorithm for the hypervolume indicator. In IEEE Congress on Evolutionary
  Computation, pages 1157-1163, Vancouver, Canada, July 2006.
  Minimization is implicitly assumed here!
  """
  def __init__(self, reference):
    self.reference = reference
    self.list = None

  def compute(self, front):
    """
    Returns the hyper-volume that is dominated by a non-dominated front.
    Before the HV computation, front and reference point are translated, so
    that the reference point is [0, ..., 0].
    :param front:
    :return: hyper-volume value
    """
    def weak_dominate(one, two):
      """
      Check if one dominates two
      :param one: First set of objectives
      :param two: Second set of objectives
      :return:
      """
      for i in xrange(len(one)):
        if one[i] > two[i]:
          return False
      return True

    relevants = []
    reference = self.reference
    d = len(reference)
    for point in front:
      if weak_dominate(point, reference): relevants.append(point)

    if any(reference):
      for j in xrange(len(relevants)):
        relevants[j] = [relevants[j][i] - reference[i] for i in xrange(d)]
    self.pre_process(relevants)
    bounds = [-1.0e308]*d
    return self.recurse(d-1, len(relevants), bounds)

  def recurse(self, d, length, bounds):
    """
    Recursive call for hyper volume calculation.
    In contrast to the paper, the code assumes that the reference point
    is [0, ..., 0]. This allows the avoidance of a few operations.
    :param d: Dimension Index
    :param length: Number of relevant points
    :param bounds: Bounding Values
    :return: hyper-volume
    """
    hvol = 0.0
    sentinel = self.list.sentinel
    if length == 0:
      return hvol
    elif d == 0:
      # Single Dimension
      return -sentinel.next[0].value[0]
    elif d == 1:
      # 2 dimensional problem
      q = sentinel.next[1]
      h = q.value[0]
      p = q.next[1]
      while p is not sentinel:
        p_value = p.value
        hvol += h * (q.value[1] - p_value[1])
        if p_value[0] < h:
          h = p_value[0]
        q = p
        p = q.next[1]
      hvol += h * q.value[1]
      return hvol
    else:
      remove = MultiList.remove
      reinsert = MultiList.reinsert
      recurse = self.recurse
      p = sentinel
      q = p.prev[d]
      while q.value is not None:
        if q.ignore < d:
          q.ignore = 0
        q = q.prev[d]
      q = p.prev[d]
      while length > 1 and (q.value[d] > bounds[d] or q.prev[d].value[d] >= bounds[d]):
        p = q
        remove(p, d, bounds)
        q = p.prev[d]
        length -= 1
      q_area = q.area
      q_value = q.value
      q_prev_d = q.prev[d]
      if length > 1:
        hvol = q_prev_d.volume[d] + q_prev_d.area[d] * (q_value[d] - q_prev_d.value[d])
      else:
        q_area[0] = 1
        q_area[1:d+1] = [q_area[i] * -q_value[i] for i in xrange(d)]
      q.volume[d] = hvol
      if q.ignore >= d:
        q_area[d] = q_prev_d.area[d]
      else:
        q_area[d] = recurse(d-1, length, bounds)
        if q_area[d] < q_prev_d.area[d]:
          q.ignore = d
      while p is not sentinel:
        p_value_d = p.value[d]
        hvol += q.area[d] * (p_value_d - q.value[d])
        bounds[d] = p_value_d
        reinsert(p, d, bounds)
        length += 1
        q = p
        p = p.next[d]
        q.volume[d] = hvol
        if q.ignore >= d:
          q.area[d] = q.prev[d].area[d]
        else:
          q.area[d] = recurse(d-1, length, bounds)
          if q.area[d] <= q.prev[d].area[d]:
            q.ignore = d
      hvol - q.area[d] * q.value[d]
      return hvol

  def pre_process(self, front):
    d = len(self.reference)
    multi_list = MultiList(d)
    nodes = [MultiList.Node(d, point) for point in front]
    for i in xrange(d):
      HyperVolume.dimension_sort(nodes, i)
      multi_list.extend(nodes, i)
    self.list = multi_list

  @staticmethod
  def dimension_sort(nodes, i):
    decorated = [(node.value[i], node) for node in nodes]
    decorated.sort()
    nodes[:] = [node for (_, node) in decorated]

  @staticmethod
  def get_reference_point(problem, points):
    reference = [-sys.maxint if obj.to_minimize else sys.maxint for obj in problem.objectives]
    for point in points:
      for i, obj in enumerate(problem.objectives):
        if obj.to_minimize:
          if point[i] > reference[i]:
            reference[i] = point[i]
        else:
          if point[i] < reference[i]:
            reference[i] = point[i]
    for i, obj in enumerate(problem.objectives):
      if obj.to_minimize:
        reference[i] += 1
      else:
        reference[i] -= 1
    return reference


class MultiList:
  """A special data structure needed by FonsecaHyperVolume.
  It consists of several doubly linked lists that share common nodes. So,
  every node has multiple predecessors and successors, one in every list.
  """
  class Node:
    def __init__(self, count, value=None):
      self.value = value
      self.next = [None] * count
      self.prev = [None] * count
      self.ignore = 0
      self.area = [0.0] * count
      self.volume = [0.0] * count

    def __str__(self):
      return str(self.value)

  def __init__(self, count):
    """
    Build 'count' number of doubly linked lists.
    :param count: Number of doubly linked lists
    :return:
    """
    self.count = count
    self.sentinel = MultiList.Node(count)
    self.sentinel.next = [self.sentinel] * count
    self.sentinel.prev = [self.sentinel] * count

  def __str__(self):
    strings = []
    for i in xrange(self.count):
      current_list = []
      node = self.sentinel.next[i]
      while node != self.sentinel:
        current_list.append(str(node))
        node = node.next[i]
      strings.append(str(current_list))
    string_repr = ""
    for string in strings:
      string_repr += string + "\n"
    return string_repr

  def __len__(self):
    """
    Returns the number of lists that are included in this MultiList.
    """
    return self.count

  def size(self, index):
    """
    Returns the length of the i-th list.
    """
    length = 0
    sentinel = self.sentinel
    node = sentinel.next[index]
    while node != sentinel:
      length += 1
      node = node.next[index]
    return length

  def append(self, node, index):
    """
    Appends a node to the end of the list at the given index.
    :param node: Node to be appended
    :param index: Index of list to be appended into
    """
    penultimate = self.sentinel.prev[index]
    node.next[index] = self.sentinel
    node.prev[index] = penultimate
    self.sentinel.prev[index] = node
    penultimate.next[index] = node

  def extend(self, nodes, index):
    """
    Extend the list at the given index with nodes
    :param nodes: Nodes to be appended
    :param index: Index of list to be extended
    """
    sentinel = self.sentinel
    for node in nodes:
      penultimate = sentinel.prev[index]
      node.next[index] = sentinel
      node.prev[index] = penultimate
      sentinel.prev[index] = node
      penultimate.next[index]= node

  @staticmethod
  def remove(node, index, bounds):
    """
    Removes and returns node from all lists in [0, index]
    :param node: Node to be removed
    :param index: Index to be removed till
    :param bounds:
    :return: Removed node
    """
    for i in xrange(index):
      pred = node.prev[i]
      succ = node.next[i]
      pred.next[i] = succ
      succ.prev[i] = pred
      if bounds[i] > node.value[i]:
        bounds[i] = node.value[i]
    return node

  @staticmethod
  def reinsert(node, index, bounds):
    """
    Inserts 'node' at the position it had in all lists in [0, 'index'[
    before it was removed. This method assumes that the next and previous
    nodes of the node that is reinserted are in the list.
    :param node: Node to be reinserted
    :param index: Index to be reinserted at
    :param bounds:
    """
    for i in xrange(index):
      node.prev[i].next[i] = node
      node.next[i].prev[i] = node
      if bounds[i] > node.value[i]:
        bounds[i] = node.value[i]


def _test():
  reference_point = [2,2,2]
  hv = HyperVolume(reference_point)
  front = [[1,0,1], [0,1,0]]
  print(hv.compute(front))

# if __name__ == "__main__":
#   _test()

"""A12 Faster Version
"""
class o():
  "Anonymous container"
  def __init__(i,**fields) : 
    i.override(fields)
  def override(i,d): i.__dict__.update(d); return i
  def __repr__(i):
    d = i.__dict__
    name = i.__class__.__name__
    return name+'{'+' '.join([':%s %s' % (k,d[k]) 
                     for k in i.show()])+ '}'
  def show(i):
    return [k for k in sorted(i.__dict__.keys()) 
            if not "_" in k]
            
def a12(lst1,lst2,small=0.56):
  "how often is x in lst1 more than y in lst2?"
  def loop(t,t1,t2): 
    while t1.j < t1.n and t2.j < t2.n:
      h1 = t1.l[t1.j]
      h2 = t2.l[t2.j]
      h3 = t2.l[t2.j+1] if t2.j+1 < t2.n else None 
      if h1>  h2:
        t1.j  += 1; t1.gt += t2.n - t2.j
      elif h1 == h2:
        if h3 and h1 > h3 :
            t1.gt += t2.n - t2.j  - 1
        t1.j  += 1; t1.eq += 1; t2.eq += 1
      else:
        t2,t1  = t1,t2
    return t.gt*1.0, t.eq*1.0
  #--------------------------
  lst1 = sorted(lst1, reverse=True)
  lst2 = sorted(lst2, reverse=True)
  n1   = len(lst1)
  n2   = len(lst2)
  t1   = o(l=lst1,j=0,eq=0,gt=0,n=n1)
  t2   = o(l=lst2,j=0,eq=0,gt=0,n=n2)
  gt,eq= loop(t1, t1, t2)
  return gt/(n1*n2) + eq/2/(n1*n2) < 0.56

def sampleWithReplacement(lst):
  "returns a list same size as list"
  def any(n)  : return random.uniform(0,n)
  def one(lst): return lst[ int(any(len(lst))) ]
  return [one(lst) for _ in lst]

"""


Then, for all those samples,
 check if some *testStatistic* in the original pair
hold for all the other pairs. If it does more than (say) 99%
of the time, then we are 99% confident in that the
populations are the same.

In such a _bootstrap_ hypothesis test, the *some property*
is the difference between the two populations, muted by the
joint standard deviation of the populations.

"""
def testStatistic(y,z): 
    """Checks if two means are different, tempered
     by the sample size of 'y' and 'z'"""
    tmp1 = tmp2 = 0
    for y1 in y.all: tmp1 += (y1 - y.mu)**2 
    for z1 in z.all: tmp2 += (z1 - z.mu)**2
    s1    = (float(tmp1)/(y.n - 1))**0.5
    s2    = (float(tmp2)/(z.n - 1))**0.5
    delta = z.mu - y.mu
    if s1+s2:
      delta =  delta/((s1/y.n + s2/z.n)**0.5)
    return delta
"""

The rest is just details:

+ Efron advises
  to make the mean of the populations the same (see
  the _yhat,zhat_ stuff shown below).
+ The class _total_ is a just a quick and dirty accumulation class.
+ For more details see [the Efron text][efron01].  

"""
def bootstrap(y0,z0,conf=0.01,b=10000):
  """The bootstrap hypothesis test from
     p220 to 223 of Efron's book 'An
    introduction to the boostrap."""
  class total():
    "quick and dirty data collector"
    def __init__(i,some=[]):
      i.sum = i.n = i.mu = 0 ; i.all=[]
      for one in some: i.put(one)
    def put(i,x):
      i.all.append(x);
      i.sum +=x; i.n += 1; i.mu = float(i.sum)/i.n
    def __add__(i1,i2): return total(i1.all + i2.all)
  y, z   = total(y0), total(z0)
  x      = y + z
  tobs   = testStatistic(y,z)
  yhat   = [y1 - y.mu + x.mu for y1 in y.all]
  zhat   = [z1 - z.mu + x.mu for z1 in z.all]
  bigger = 0.0
  for i in range(b):
    if testStatistic(total(sampleWithReplacement(yhat)),
                     total(sampleWithReplacement(zhat))) > tobs:
      bigger += 1
  return bigger / b < conf
