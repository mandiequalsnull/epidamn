from matplotlib import pyplot as plt
import math
from decimal import Decimal


real_data = [11754,
16315,
19258,
23040,
26512,
29331,
32381,
34505,
36907,
38817,
40120,
40072,
54075,
58829,
59637,
60361,
60677,
60786,
59520,
58022,
57953,
55713,
55591,
54343,
52510,
51013,
49479,
47413,
46231,
45655,
44707,
44615,
43953,
44089,
45934,
47477,
49140,
51070,
54178,
58862,
60019,
74942,
83475,
91413,
103458,
116328,
131602,
157751,
184764,
212852,
239777,
277329,
310261,
353824,
407441,
462376,
521291]
# real_data += [None]*100

def S(x, s1, h1, s2, hs):
	return h1 - ((h1 + s2) / (1 + math.e**(-1*(x)/s1 + hs)))

def get_scores(s1, h1, s2, hs, ds, d):
	pass

def foo(s1, h1, s2, hs, ds, d, display=True):
	ds = int(ds)
	# s = int(sys.argv[1])*2
	X1 = [i for i in range(len(real_data))] # real X-axis points
	X2 = [i for i in range(len(real_data)+100)] # estimated X-axis points
	Y = [S(x, s1, h1, s2, hs) for x in X2] # Y-axis points
	# used to divide S(adsada) by d

	if display:
		plt.cla()
		axes = plt.gca()
		# axes.set_xlim([xmin,xmax])
		axes.set_ylim([-3,10])
		plt.plot(X2,Y) # Plotting the line plot
		plt.savefig('foo.png') #Displaying the plot

	Y2 = [1]
	for i in range(1,len(X2)):
		Y2 += [Y2[-1]*Y[i]]
	Y2 = [y/d for y in Y2]


	guess_data_dict = {X2[i]+ds: Y2[i] for i in range(len(Y2))}
	real_data_dict = {X1[i]: real_data[i] for i in range(len(real_data))}

	score = sum([abs(real_data_dict[i] - guess_data_dict.get(i, 0))**2 for i in real_data_dict.keys()])
	# for i in real_data_dict.keys():
	# 	print(real_data_dict[i])
	# print('%.2E' % Decimal(str(score)))

	if display:
		plt.cla()
		plt.plot([x+ds for x in X2],Y2,color="green") # Plotting the line plot
		plt.plot(X1,real_data,color="red")
		plt.savefig('foo2.png') #Displaying the plot

	return score
# foo(2,2,3,4)
# foo(10)