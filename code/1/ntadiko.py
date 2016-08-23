#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ntadiko


"""
import sys,math,random
from collections import Counter
sys.dont_write_bytecode=True

def ShanonsEntropy(arr):
	"""
	The number of bits required to represent the Uncertainity.

	For  example, if we have 4 users in an anonymous system, then the probablity to identify
	one user as the sender/receiver is 1/4. Then Shanons entropy will be 
	S = sum( p * logp)
	S = 4 * -1/4 log(1/4) = 2
	"""
	if type(arr) is list:
		su=0
		for i,v in enumerate(arr):
			su=su+ (-1*v*math.log(v,2))
		return su
	return arr*math.log(arr,2)

def birthdayParadoxFindPair(arr):
	"""
	In probability theory, the birthday problem or birthday paradox[1] concerns the probability 
	that, in a set of {\displaystyle n} n randomly chosen people, some pair of them will have the
	same birthday. By the pigeonhole principle, the probability reaches 100% when the number of 
	people reaches 367 (since there are only 366 possible birthdays, including February 29). 
	However, 99.9% probability is reached with just 70 people, and 50% probability with 23 people.
	These conclusions are based on the assumption that each day of the year (except February 29) is
	equally probable for a birthday.
	"""
	dic = dict(Counter(arr))
	for k,v in dic.iteritems():
		if v>1:
			return True
	return False

def birthdayParadox(trials, size):
	"""birthdayParadox

	Args:
	    trials (int): Number of trials.
	    size (int): size of the group.

	Returns:
	    float: The  if successful, False otherwise.

	"""
	count=0
	for i in range(trials):
		if birthdayParadoxFindPair([random.randint(1,365) for i in range(size)]):
			count=count+1
	return float(count)/trials

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