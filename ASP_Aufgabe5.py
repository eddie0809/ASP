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
	[10**-5, 0, 0, 10**5, 0, 10**5],
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
	#print("Ich bin in der Function: ", L)
	for J in range(0, 6):
		if J == I:
			probIJ[J] = np.float64(0)
		else:
			#print(L[I,I])
			probIJ[J] = -1. * L[J,I]/L[I,I] # probability that the state I goes to J
	partition = np.float64(0)
	#print(r2, sum(probIJ))
	if r2 <= sum(probIJ):
		for i in range(0,6):
			partition = partition + probIJ[i]
			if r2 <= partition:
				return i
				#if i == 5:
				#	return 5
			elif partition < r2 and i < 5:
				continue
			else:
				return i
	else:
		#print("Ich bin hier")
		return I

i = 0
t = 0


time = []

while j <= 10**6:
	while i != 3:
		i = nextState(i, L)
		t = t + lifetime(i, L)
	time.append(t)
	j = j+1
	i = 0
	t = 0	
logbins = np.logspace(np.log10(10**-8),np.log10(10**3),10**4)
plt.hist(time, logbins)
plt.xscale("log")
plt.xlim(10**-8, 10**3)
plt.show()

"""
while 1==1:
	if i % 3 == 0:
		break
	else:
		t = t + lifetime(i,L)
		helpme = nextState(i,L)
		i = helpme
		print("ich bin in der while schleife: ", i, helpme)
		#I = nextState(I,L)
		continue"""
	

