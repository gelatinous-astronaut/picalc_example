#!/usr/bin/python3

import numpy as np
import time, os
from monte_carlo import monte_carlo_simulation

if __name__ == "__main__":
	
	print('*'*35)
	print('running serial version of picalc')
	print('*'*35)

	total_n_points = 100000
	print('performing calculation with '+str(total_n_points)+' points')

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


