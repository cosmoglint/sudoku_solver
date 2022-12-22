import pprint
themat = [[8,0,5,0,2,0,0,0,6],
	[0,6,0,3,0,0,0,1,0],
	[7,0,0,0,0,6,0,3,0],
	[0,0,0,0,0,0,0,4,5],
	[0,0,7,6,0,0,0,9,0],
	[0,0,1,0,0,0,6,0,0],
	[0,0,4,0,0,8,0,0,0],
	[0,0,0,0,5,0,0,0,0],
	[2,0,3,1,7,0,0,6,0]]

def possible(x,y,n):
	global themat
	for i in range(9):
		if themat[i][y] == n:
			return False
		elif themat[x][i] == n:
			return False
	for i in range((x//3)*3,(x//3)*3+3):
		for j in range((y//3)*3,(y//3)*3+3):
			if themat[i][j] == n:
				return False
	return True

def solve():
	for i in range(9):
		for j in range(9):
			if themat[i][j] == 0:
				for n in range(1,10):
					if possible(i,j,n):
						themat[i][j] = n
						solve()
						themat[i][j] = 0
				return
	pprint.pprint(themat)
    # unimplemented for more solutions. figure out a way
	input("more solutions?")

solve()
