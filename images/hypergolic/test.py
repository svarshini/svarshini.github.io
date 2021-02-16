import numpy as np 
import matplotlib.pyplot as plt 

plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
	[50.2268, 44.0286, 38.7436, 42.7102, 38.2968, 59.1942, 59.2488, 53.6022,
	58.4674, 53.169, 54.2582], 'b-o')
plt.axis([0, 12, 0, 70])
plt.ylabel('Average Cone Angle')
plt.xlabel('Pressure')

plt.grid()
plt.show()