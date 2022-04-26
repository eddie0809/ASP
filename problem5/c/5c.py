import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt

# for using tex formatting and font in plots

plt.rcParams.update({"text.usetex": True,}) 
mpl.rcParams['text.latex.preamble'] = [r'\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{lmodern}\inputencoding{utf8}\usepackage{amsmath}\usepackage{amssymb}\usepackage{mathtools}']
mpl.rcParams['font.family'] = ['serif']


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

L = np.zeros((6,6))

for i in range(0,6):
	sumdings = 0
	for j in range(0,6):
		for k in range(0,6): # although the sum is k =/= i, for k = i the matrix returns 0 so it doesnt matter
			sumdings = sumdings + rates[i][k]
		L[i,j] = (1 - kron(i,j)) * rates[j][i] - kron(i,j) * sumdings
		# [L]_{i,j} = (1 - δ_{ij})w_{ji} - δ_{ij}Σ_{k≠i}w_{ik}
		sumdings = 0
		


# STEP 2 ON THE PROBLEM SHEET

# LIFETIME OF STATES:


def lifetime(I, L):
	r1 = np.float64(random.uniform(0,1))
	gamma = -1. * np.diagonal(L) # decay rate
	tau = 1/gamma[I] * np.log(1/r1) # lifetime, randomly generated
	return tau


# STEP 3 ON THE PROBLEM SHEET


def nextState(I, L): # it needs the generator matrix L and the initial state I
	r2 = np.float64(random.uniform(0,1))
	probIJ = [0,0,0,0,0,0] # i just need this to have 6 elements
	for J in range(0, 6):
		if J == I:
			probIJ[J] = np.float64(0) # this breaks if its not float64, dont ask why
		else:
			probIJ[J] = -1. * L[J,I]/L[I,I] # probability that the state I goes to J
	partition = np.float64(0) # see above
	r2 = np.float64(random.uniform(0,sum(probIJ)))
	for i in range(0,6):
		partition = partition + probIJ[i]
		if r2 <= partition:
			return i
		elif partition < r2 and i < 5:
			continue
		else:
			return i

I = 0 # this is actually part of step 1, but for me it makes more sense to do it here
t = 0 # - " - 
j = 0
time = []

while j <= 10**7: # number of trajectories simulated, here i use 1e7, required are 1e6
	while I != 3:
		t = t + lifetime(I, L)
		I = nextState(I, L)
	print(np.log10(j)) # i like to see the progress x)
	time.append(t)
	j = j+1
	I = 0
	t = 0

logbins = np.logspace(np.log10(10**-8), np.log10(10**3), 1000) # create bins with logarithmic scaling
plt.hist(time, logbins)
plt.title("Distribution for the first folding time $T$ ($I(0) = 0$ $\\rightarrow$ $I(T) = 3$)")
plt.xscale("log") # logarithmic timescale to compare with S13 on supplementary materials of the paper
plt.xlabel("Folding time [s]")
#plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
plt.tick_params(
    axis='y',         # changes apply to the y-axis
    which='both',     # both major and minor ticks are affected
    right=False,      # ticks along the right edge are off
    left=False,       # ticks along the left edge are off
    labelleft=False)  # labels along the left edge are off
plt.xlim(10**-8, 10**3)
plt.ylabel("Probability [AU]")
plt.savefig("ASP-5c-guuut-plot.pdf")
plt.show()
	
