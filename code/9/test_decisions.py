#!/usr/bin/python
# coding:utf8

__author__ = "ntadiko"

from random import random, seed
from unittest import TestCase, main


from decisions import enumTypeDecision, floatTypeDecision, enumTypeDecision

class Test_enumTypeDecision(TestCase):
    @classmethod
    def setUpClass(cls):
        print "\n====| %s |========================"%(cls.__name__)
        seed(0)
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)
        self.enumTypeDecision=enumTypeDecision(name="x",bounds=(0,10))
        print self.enumTypeDecision
    def test_isInBounds(self):
        self.assertFalse(self.enumTypeDecision.isInBounds(30))
        self.assertTrue(self.enumTypeDecision.isInBounds(5))

    def test_random(self):
        value = self.enumTypeDecision.random()
        self.assertLessEqual(value, self.enumTypeDecision.bounds[1] )
        self.assertGreaterEqual(value, self.enumTypeDecision.bounds[0])

    def test_limitToBounds(self):
        self.assertEqual(self.enumTypeDecision.limitToBounds(30), 10)
        self.assertEqual(self.enumTypeDecision.limitToBounds(-2), 0)

    def test_count(self):
        print list(self.enumTypeDecision.count(steps=1000))

    def test_mutate(self):
        print self.enumTypeDecision.mutate(7)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class Test_floatTypeDecision(TestCase):
    @classmethod
    def setUpClass(cls):
        print "\n====| %s |========================"%(cls.__name__)
        seed(0)
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)
        self.floatTypeDecision=floatTypeDecision(name="f",bounds=(0,1))

    def test_random(self):
        value = self.floatTypeDecision.random()
        print value

    def test_iterate(self):
        # print list(self.floatTypeDecision)
        pass

    def test_mutate(self):
        value = self.floatTypeDecision.random()
        print value
        mutatedvalue=self.floatTypeDecision.mutate(value)
        print mutatedvalue
        self.assertIsNot(value, mutatedvalue)

    def test_count(self):
        # print list(self.floatTypeDecision.count(steps=1000))
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class Test_enumTypeDecision(TestCase):
    @classmethod
    def setUpClass(cls):
        print "\n====| %s |========================"%(cls.__name__)
        seed(0)
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)
        self.enumTypeDecision=enumTypeDecision(name="x",values=["zero","one","two","three","four","five","six"])
        print self.enumTypeDecision

    def test_isInBounds(self):
        self.assertFalse(self.enumTypeDecision.isInBounds(30))
        self.assertTrue(self.enumTypeDecision.isInBounds(5))

    def test_random(self):
        value = self.enumTypeDecision.random()
        print value

    def test_limitToBounds(self):
        self.assertEqual(self.enumTypeDecision.limitToBounds(30), 2)
        self.assertEqual(self.enumTypeDecision.limitToBounds(7), 0)

    def test_count(self):
        print list(self.enumTypeDecision.count(steps=1000))

    def test_mutate(self):
        print self.enumTypeDecision.mutate("one")

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