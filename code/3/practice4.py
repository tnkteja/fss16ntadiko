#!/usr/bin/python
from __future__ import division,print_function
import sys,random,os,pprint,bisect
sys.dont_write_bytecode=True

# usage:
#   python fsm.py 21083 # for a long-ish run
#   python fsm.py 1     # for a short run

#----------------------------------------------
def fsm0():
  m     = Machine()
  print("## Initialising the states")
  sober = m.state("sober") # first names state is "start"
  print(sober)
  drunk = m.state("drunk")
  print(drunk)
  passout  = m.state("passout.") # anything with a "." is a "stop"
  print(passout)
  print("## Adding all the Trans")
  m.trans(T(sober,  take_drink, drunk),
          T(drunk, take_drink, drunk, prob=20),
          T(drunk, take_drink, passout, prob=80),
          T(sober, dont_take_drink, sober)
          )
  return m

#----------------------------------------------

def take_drink(w,trans):    return True
def dont_take_drink(w, trans):  return random.random() > 0.5

def ok (w,a):   return maybe() 
def fail(w,a):  return maybe() 
def again(w,a): return maybe()

#---------------------------------------------
def kv(d):
  return '('+', '.join(['%s: %s' % (k,d[k])
          for k in sorted(d.keys())
          if k[0] != "_"]) + ')'

def shuffle(lst):
    random.shuffle(lst)
    return lst

class Pretty(object):
  def __repr__(self):
    return self.__class__.__name__ + kv(self.__dict__) + "( id:" + str(id(self)) + " )"
    
class o(Pretty):
  def __init__(self, **adds): self.__dict__.update(adds)


#----------------------------------------------
class State(Pretty):
  def __init__(self,name): self.name, self.out, self.visits = name,[],0
  def stop(self)         : return self.name[-1] == "."
  def looper(self)       : return self.name[0] == "#"
  def arrive(self):
    print(self.name)
    if not self.looper():
      self.visits += 1
      assert self.visits <= 5, 'loop detected'

  def make_trans_choice_distribution(self):
    if not self.out:
      self.trans_choice_dist=[100]
      return
    self.trans_choice_dist=[self.out[0].prob]
    for i in xrange(1,len(self.out)):
      self.trans_choice_dist.append(self.trans_choice_dist[i-1]+self.out[i].prob)

  def next(self,w):
    if not self.out:
      return self
    tran=self.out[bisect.bisect(self.trans_choice_dist,int(random.random() * self.trans_choice_dist[-1]))]
    if tran.gaurd(w,tran):
          return tran.there
    return self
  
class Trans(Pretty):
  def __init__(self,here,gaurd,there,prob=100):
    self.here,self.gaurd,self.there,self.prob = here, gaurd, there, prob

T= Trans    

class Machine(Pretty):
  def __init__(self):
    self.states={}
    self.first = None
  def state(self,txt):
    tmp = State(txt)
    self.states[txt] = tmp
    self.first = self.first or tmp
    return tmp
  def trans(self,*trans):
    for tran in trans:
      tran.here.out += [tran]
    for state in self.states.values():
      state.make_trans_choice_distribution()

  def run(self,seed = 1):
   print('#', seed)
   random.seed(seed)
   w, here = o(), self.first 
   while True:
     here.arrive()
     if here.stop():
       return w
     else:
       here = here.next(w)

if __name__ == '__main__':
  if len(sys.argv)>1:
     fsm0().run(int(sys.argv[1]))
  else:
     fsm0().run(random.randint(1,10**3))


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