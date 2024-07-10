#!/usr/bin/python3

import numpy as np
import time, os

total_n_points = input("enter number of points [10,000]: ")
try:
    total_n_points = int(total_n_points)
except:
    total_n_points = 10000

print('performing calculation with '+str(total_n_points)+' points')

def monte_carlo_simulation(n_points):
	circle_count = 0	
	
	for i in np.arange(n_points):
		new_point = np.array([2.*(np.random.random()-0.5),2*(np.random.random()-0.5)])
		
		if np.linalg.norm(new_point) < 1:
			circle_count += 1

	return circle_count

if __name__ == "__main__":
	
	print('*'*35)
	print('running serial version of picalc')
	print('*'*35)

	starttime = time.time()
	final_circle_count = monte_carlo_simulation(total_n_points)
	endtime = time.time()

	pi_est = 4.0*final_circle_count/total_n_points
	percent_diff = (pi_est - np.pi)/np.pi * 100

	print('time taken to complete: {:.8f}s'.format(endtime - starttime))
	print('number of points generated: ',total_n_points)
	print('number of points in circle: ',final_circle_count)
	print('estimate of pi: ',pi_est)
	print('percent difference: ',np.round(percent_diff,2),'%')


