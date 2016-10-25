#!/usr/bin/python
# coding: utf-8
"""
"""
__author__ = "ntadiko"



from problems import schaffer,osyczka2,kursawe
from optimizers import sa,mws

for problem in [schaffer,osyczka2,kursawe]:
    for optimizer in [sa,mws]:
        problem(optimizer=optimizer()).solve()
        print '\n\n'+"-"*80+'\n\n'
#can be  solve(), study()

#schaffer(optimizer=sa()).solve()
# osyczka2(optimizer=sa()).solve()
# osyczka2(optimizer=mws()).solve()