#!/usr/bin/python
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

import ntadiko,utest,random

@utest.ok
def entropyFor4():
	arr=[0.25,0.25,0.25,0.25]
	ans=ntadiko.ShanonsEntropy(arr)
	assert ans == 2.0

@utest.ok
def birthdayParadox23():
	assert ntadiko.birthdayParadox(10000, 23) >= 0.5

@utest.ok
def birthdayParadox70():
	assert ntadiko.birthdayParadox(10000, 70) >= 0.999

@utest.ok
def birthdayParadox70E():
	assert ntadiko.birthdayParadox(10000, 70 ) <= 0.9


utest.oks()