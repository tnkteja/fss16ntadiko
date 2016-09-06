class board(object):
	"""docstring for board"""
	def __init__(self,x):
		self.N=x
		self.board = [ [ '.' for j in xrange(x)] for i in xrange(x)]
		 
	def __getitem__(self,i):
		return self.board[i]

	def place_queen(self,x0,y0):
		x,y=x0,y0
		if self.board[x][y] !='.':
			return False
		else:
			# along x,y
			for i in xrange(self.N):
				self.board[x][i]='X'
				self.board[i][y]='X'
		
			# diagonally
			for i in xrange(min(x,y)):
				x-=1
				y-=1
		
			for i in xrange(0,(self.N-max(x,y))):
				self.board[x+i][y+i]='X'
			x,y=x0,y0
			i=0
			while 0 <= x+i <= (self.N-1) and 0 <= y-i <= (self.N-1):
				self.board[x+i][y-i]='X'
				i+=1
			x,y=x0,y0
			i=0
			while 0 <= x-i <= (self.N-1) and 0 <= y+i <= (self.N-1):
				self.board[x-i][y+i]='X'
				i+=1
				
			self.board[x0][y0]='Q'
			
	def available_positions(self):
		for x,row in enumerate(self.board):
			for y,col in enumerate(row):
				if col == '.':
					yield x,y



	def __repr__(self):
		n=self.N*4+1
		return  n*'-'+'\n'+('\n'+n*'-'+'\n').join(['| '+' | '.join(row)+' |' for row in self.board])+'\n'+n*'-'

import copy,random
def search(board,queens):
	avp=list(board.available_positions())

	if not avp or queens==0:
		return
	if len(avp)==1 and queens==1:
		return [avp]
	if len(avp)==1 and queens >1:
		return
	sols=[]
	for av in avp:
		b=copy.deepcopy(board)
		b.place_queen(*av)
		r=search(b,queens-1)
		tmp=[av]
		if r:
	
			for i in r:
				sols.append(tuple(sorted(tmp+i)))
	return [list(sol) for sol in set(sols)]

b=board(8)
import time
start=time.time()
x=search(b,queens=len(b.board))
end=time.time()
print "time: ",end-start
print "Solutions:",len(x),'\n'

for i,sol in enumerate(x):
	print "#"*5+" Solution "+str(i+1)+' '+"#"*5
	bb=board(len(b.board))
	for pos in sol:
		bb.place_queen(*pos)
	print bb