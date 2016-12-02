#!/usr/bin/python
# coding:utf8

__author__ = "ntadiko"

from random import random, seed
from unittest import TestCase, main


from optimizers import sa
from problems import osyczka2

class Test_sa(TestCase):
    @classmethod
    def setUpClass(cls):
        print "\n====| %s |========================"%(cls.__name__)
        seed(0)
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)

    def test_optimizer(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class Test_mws(TestCase):
    @classmethod
    def setUpClass(cls):
        print "\n====| %s |========================"%(cls.__name__)
        seed(0)
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)
        
    def test_optimizer(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class Test_de(TestCase):
    @classmethod
    def setUpClass(cls):
        print "\n====| %s |========================"%(cls.__name__)
        seed(0)
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)
        
    def test_optimizer(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    main()

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