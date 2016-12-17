#!/usr/bin/python
# coding:utf8

__author__ = "ntadiko"

from pprint import pprint
from unittest import TestCase, main
from random import random


from decisions import intTypeDecision
from dsl import problem,objective, population
from objectives import functionTypeObjective

class Test_problem(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trials = 10000
        cls.paretoFrontier1=[[0.02095599670188364, 0.6778384360925239, 0.7857142857142857, 0.0], [0.034180361870042086, 0.5245208866135824, 0.8840579710144928, 0.1029411764705882], [0.02460798746756646, 0.6521854957069885, 1.0, 0.30000000000000004], [0.02189842089944057, 0.5463625723374128, 0.6833333333333333, 0.046511627906976716], [0.03164888468336628, 0.383529865014307, 0.8513513513513513, 0.08695652173913049], [0.06454575880596088, 0.5903604706736836, 0.7592592592592593, 0.0888888888888889], [0.0915939211696852, 0.5201361891509115, 0.8497109826589595, 0.10365853658536583], [0.030876798455713686, 0.5110022993045705, 0.8301886792452831, 0.29032258064516125], [0.05191147906812763, 0.49380105682129466, 1.0, 0.0], [0.009234201362161954, 0.5003031613530177, 0.5, 0.0]]
        cls.paretoFrontier2=[[0.08738234913396675, 0.653748187881778, 0.712707182320442, 0.0], [0.09958142712660678, 0.772687573987016, 0.6884057971014492, 0.0], [0.06966259780901314, 0.5721201437854408, 0.9736842105263158, 0.22916666666666663], [0.04042797689964187, 0.5813219864656675, 0.7777777777777778, 0.0], [0.04313029690826623, 0.5991287479074885, 0.75, 0.0], [0.055610178628247874, 0.7660031282960829, 0.9285714285714286, 0.5357142857142857], [0.07798260806583651, 0.4374363614005098, 0.9435483870967742, 0.26875000000000004], [0.10299750041157082, 0.5396698782151578, 0.6608695652173913, 0.0], [0.09873984318665308, 0.688981118336843, 0.9225806451612903, 0.192090395480226], [0.0432321245546386, 0.687228966713076, 0.9230769230769231, 0.2941176470588235]]
        cls.paretoFrontier3=[[0.018667164751246072, 0.6725435355538931, 1.0, 0.0], [0.03236982922166506, 0.8929704175715291, 1.0, 0.0], [0.012577365172705437, 0.5902742693038511, 0.9166666666666666, 0.0], [0.030033915594442736, 0.7243922217565271, 0.9166666666666666, 0.47619047619047616], [0.016242942533825754, 0.7450106084771029, 0.8888888888888888, 0.33333333333333337], [0.031970980789334746, 0.6408347041400978, 0.8947368421052632, 0.0], [0.07765335322416529, 0.5706053874436364, 0.8695652173913043, 0.0], [0.03600347879002345, 0.720057256147724, 0.8888888888888888, 0.6190476190476191], [0.019042558918572212, 0.5815385685664295, 0.9574468085106383, 0.27419354838709675], [0.018872487087262576, 0.5309957865555107, 1.0, 0.3157894736842105]]
        cls.referenceSet=[[0.018667164751246072, 0.6725435355538931, 1.0, 0.0], [0.03236982922166506, 0.8929704175715291, 1.0, 0.0], [0.012577365172705437, 0.5902742693038511, 0.9166666666666666, 0.0], [0.031970980789334746, 0.6408347041400978, 0.8947368421052632, 0.0], [0.02095599670188364, 0.6778384360925239, 0.7857142857142857, 0.0], [0.07765335322416529, 0.5706053874436364, 0.8695652173913043, 0.0], [0.09958142712660678, 0.772687573987016, 0.6884057971014492, 0.0], [0.08738234913396675, 0.653748187881778, 0.712707182320442, 0.0], [0.06966259780901314, 0.5721201437854408, 0.9736842105263158, 0.22916666666666663], [0.05191147906812763, 0.49380105682129466, 1.0, 0.0]]

    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)
        self.problem = problem(
            decisions=[
                intTypeDecision(name='x',bounds=(-10,10))
            ],
            objectives=[
                functionTypeObjective(function=lambda x:  x**2),
                functionTypeObjective(function=lambda x:  (x-2)**2)
            ]
            )
        #print self.problem

    def test_randomSample(self):
        print self.problem.randomSample(300, withReplacement=True)

    def test_preRun(self):
        print self.problem.preRun()
        print self.problem.objectives

    def test_continuousDomination(self):
        self.problem.preRun()
        print self.problem.objectives
        oneSolution= self.problem.random()
        oneObjectives=self.problem.objectiveScores(oneSolution)
        print oneSolution, oneObjectives
        otherSolution= self.problem.random()
        otherObjectives=self.problem.objectiveScores(otherSolution)
        print otherSolution, otherObjectives
        oneObjectives=(1,1)
        otherObjectives=(1,1)
        print self.problem.continuousDomination(oneObjectives, otherObjectives)

    def test_spread(self):
        paretoFrontier1=self.__class__.paretoFrontier1
        paretoFrontier2=self.__class__.paretoFrontier2
        paretoFrontier3=self.__class__.paretoFrontier3
        referenceSet=self.__class__.referenceSet

        print self.problem.spread(paretoFrontier1, referenceSet)
        print self.problem.spread(paretoFrontier2, referenceSet)
        print self.problem.spread(paretoFrontier3, referenceSet)

    def test_interGenerationalDistance(self):
        paretoFrontier1=self.__class__.paretoFrontier1
        paretoFrontier2=self.__class__.paretoFrontier2
        paretoFrontier3=self.__class__.paretoFrontier3
        referenceSet=self.__class__.referenceSet
        print self.problem.interGenerationalDistance(paretoFrontier1, referenceSet)
        print self.problem.interGenerationalDistance(paretoFrontier2, referenceSet)
        print self.problem.interGenerationalDistance(paretoFrontier3, referenceSet)
    
    def test_hyperVolume(self):
        referencePoint=(10000,1,1,1)
        paretoFrontier1=self.__class__.paretoFrontier1
        paretoFrontier2=self.__class__.paretoFrontier2
        paretoFrontier3=self.__class__.paretoFrontier3
        print self.problem.hypervolume(paretoFrontier1, referencePoint=referencePoint)
        print self.problem.hypervolume(paretoFrontier2, referencePoint=referencePoint)
        print self.problem.hypervolume(paretoFrontier3, referencePoint=referencePoint)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class Test_optimizer(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trials = 10000
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class Test_decision(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trials = 10000
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class Test_objective(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trials = 10000
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)
        self.objective = objective()

    # def test_setPreRunMinMax(self):
    #     self.objective.setPreRunMinMax(1,23)
    #     print self.objective

    # def test_normalise(self):
    #     self.objective.setPreRunMinMax(1,23)
    #     print self.objective.normalise(20)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class Test_constraint(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trials = 10000
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

class Test_population(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trials = 10000
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)

    def test_population(self):
        p = [ round(random(),2) for i in xrange(100)]
        p=population(p)
        print p

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