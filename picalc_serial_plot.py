#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

#load the simulation the monte_carlo.py file included in this repo
from monte_carlo import monte_carlo_simulation 


n_points = 5000
circle_count = 0
radius = 1 
points = np.zeros((n_points,2))

# effectively the same as the monte_carlo.py code, 
# but we want to keep track of the exact points we create
# so that we can plot them
# (this script is less for testing performance and moreso intended to simply generate a figure)
starttime = time.time()
for i in np.arange(n_points):
	new_point = np.array([2.*(np.random.random()-0.5),2*(np.random.random()-0.5)])*radius
	points[i] = new_point
	if np.linalg.norm(new_point) < radius:
		circle_count += 1

pi_est = 4.0*circle_count/n_points
percent_diff = (pi_est - np.pi)/np.pi * 100
endtime = time.time()

print('time taken to complete: {:.8f}s'.format(endtime - starttime))
print('number of points generated: ',n_points)
print('number of points in circle: ',circle_count)
print('estimate of pi: ',pi_est)
print('percent difference: ',np.round(percent_diff,2))

distances = np.linalg.norm(points,axis=1)
points_in_circle = points[np.where(distances<radius)[0]]
points_out_circle = points[np.where(distances>=radius)[0]]

fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(5,5))
ax.plot(points_in_circle[:,0],points_in_circle[:,1],'o',mec='None',mfc='cyan',ms=3)
ax.plot(points_out_circle[:,0],points_out_circle[:,1],'o',mec='None',mfc='orange',ms=3)
circle = patches.Circle((0., 0.), radius=1, edgecolor='grey', facecolor='none')
ax.add_patch(circle)
ax.set_axis_off()
plt.show()