import numpy as np
import math
import random
import matplotlib.pyplot as plt

def kron(i,j):
	if i == j:
		return 1
	else:
		return 0

# numbers taken from table 2 in J. Stigler et al, Science 334 513 (2011) https://doi.org/10.1126/science.1207598
# no errors

rates = np.array([
	[0, 10**5.8, 10**5.8, 0, 10**5.4, 0],
	[10**-4.1, 0, 0, 10**5.6, 0, 0],
	[10**(-5), 0, 0, 10**5, 0, 10**5],
	[0, 10**(-0.8), 10**(-.7), 0, 0, 0],
	[10**(-1.4), 0, 0, 0, 0, 0],
	[0, 0, 10**(-0.13), 0, 0, 0]])

# STEP 1 ON THE PROBLEM SHEET

I = 0
t = 0
L = np.zeros((6,6))

for i in range(0,6):
	sumdings = 0
	for j in range(0,6):
		for k in range(0,6): # although the sum is k =/= i, for k = i the matrix returns 0 so it doesnt matter
			#print(i, j, k)
			sumdings = sumdings + rates[i][k]
		#print(kron(i,j), i, j)
		L[i,j] = (1 - kron(i,j)) * rates[j][i] - kron(i,j) * sumdings
		


# STEP 2 ON THE PROBLEM SHEET

# LIFETIME OF STATES:


def lifetime(I, L):
	r1 = random.uniform(0,1)
	gamma = -1. * np.diagonal(L) # decay rate
	tau = 1/gamma[I] * np.log(1/r1) # lifetime
	return tau


# STEP 3 ON THE PROBLEM SHEET


def nextState(I, L): # it needs the generator matrix L and the initial state I
	r2 = np.float64(random.uniform(0,1))
	probIJ = [0,0,0,0,0,0] # i just need this to have 6 elements
	for J in range(0, 6):
		if J == I:
			probIJ[J] = np.float64(0)
		else:
			#print(L[I,I])
			probIJ[J] = -1. * L[J,I]/L[I,I] # probability that the state I goes to J
	helper = np.float64(0)
	for i in range(0,6):
		if helper <= r2:
			helper = helper + probIJ[i]
		else:
			#print(i, helper, r2)
			return int(i-1)
			break

I = 0
t = 0

#print(np.diagonal(L))
#print(nextState(I,L))
helpme = 0
while I != 3:
	t = t + lifetime(I,L)
	helpme = nextState(I,L)
	I = helpme
	print(I, helpme)
	#I = nextState(I,L)
	

