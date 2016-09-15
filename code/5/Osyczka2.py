#!/usr/bin/python
# -*- coding: utf8 -*-

g1 = lambda x1,x2:    x1+x2 >= 2
g2 = lambda x1,x2:    x1+x2 <= 6
g3 = lambda x1,x2:    x1-x2 >= 2
g4 = lambda x1,x2:    (3*x2) - x1 >= 2
g5 = lambda x3,x4:    ((x3-3)**2) + x4 <= 4
g6 = lambda x5,x6:    True

x1x2bounds = xrange(0,11)
x3x5bounds = xrange(1,6)
x4bounds = xrange(0,7)
x5bounds = xrange(0,11)
