#!/usr/bin/python
# coding: utf-8
"""
"""
from __future__ import division

__author__ = "ntadiko"

from operator import lt, gt
from sys import dont_write_bytecode


from dsl import objective

dont_write_bytecode=True

class functionTypeObjective(objective):

    def __init__(self, function, type=lt):
        super(functionTypeObjective, self).__init__()
        self.cache={}
        self.normalisedCache={}
        self.function=function
        self.type=type

    def setType(self,type):
        self.type=type

    def score(self,*args):
        value=self.cache.get(args,False)
        if not value:
            value=self.function(*args)

        if value < self._minimumSoFar:  self._minimumSoFar=value
        elif value > self._maximumSoFar:  self._maximumSoFar=value
        return value

    def better(self,one, other):
        return self.type(one, other)

    def worse(self,one, other):
        operator= lt if self.type is gt else gt
        return operator(one, other)

    def __call__(self,*args):
        return self.score(self,*args)

"""
MIT License

Copyright (c) 2016 Neela Krishna Teja Tadikonda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""