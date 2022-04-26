import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# for using tex formatting and font in plots

plt.rcParams.update({"text.usetex": True,}) 
mpl.rcParams['text.latex.preamble'] = [r'\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{lmodern}\inputencoding{utf8}\usepackage{amsmath}\usepackage{amssymb}\usepackage{mathtools}']
mpl.rcParams['font.family'] = ['serif']


rates = np.array([
	[0, 10**5.8, 10**5.8, 0, 10**5.4, 0],
	[10**-4.1, 0, 0, 10**5.6, 0, 0],
	[10**-5, 0, 0, 10**5, 0, 10**5],
	[0, 10**(-0.8), 10**(-.7), 0, 0, 0],
	[10**(-1.4), 0, 0, 0, 0, 0],
	[0, 0, 10**(-0.13), 0, 0, 0]]) # "stolen" from myself from the 5c.py file

gamma = [0,0,0,0,0,0]
for i in range(0,6):
	gamma[i] = sum(rates[i])
print(gamma[2])
c1 = rates[0][1]*rates[1][3]/(gamma[0]-gamma[1])
c2 = rates[0][2]*rates[2][3]/(gamma[0]-gamma[2])
c1  = c1/c2
T = np.logspace(-8, 3, 10000)
func = -1. * c1 * (np.exp(-1. * T * gamma[0]) - np.exp(-1.* T*gamma[1])) - (np.exp(-1* T * gamma[0]) - np.exp(-1.* T * gamma[2]))
plt.plot(T, func)
plt.title("Probability density for $I(T)=3$ after 2 jumps")
plt.xscale("log") # logarithmic timescale to compare with S13 on supplementary materials of the paper
plt.xlim(10**-8, 10**3)
plt.xlabel("Folding time $T$ [s]")
#plt.tick_params(axis='both', which='both', bottom='off', top='off', labelbottom='off', right='off', left='off', labelleft='off')
plt.tick_params(
    axis='y',         # changes apply to the y-axis
    which='both',     # both major and minor ticks are affected
    right=False,      # ticks along the right edge are off
    left=False,       # ticks along the left edge are off
    labelleft=False)  # labels along the left edge are off
plt.ylabel("Probability [AU]")
plt.savefig("ASP-5b-plot.pdf")
plt.savefig("ASP-5b-plot.png")
plt.show()
