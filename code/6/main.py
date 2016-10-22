#!/usr/bin/python
# coding: utf-8
"""
"""
__author__ = "ntadiko"



from problems import schaffer,osyczka2,kursawe
from optimizers import sa,mws,de

# for problem in [schaffer,osyczka2,kursawe]:
#     for optimizer in [sa,mws]:
#         problem(optimizer=optimizer()).solve()
#         print "-"*80
#can be  solve(), study()

schaffer(optimizer=mws()).solve()
schaffer(optimizer=sa()).solve()
#osyczka2(optimizer=mws()).solve()