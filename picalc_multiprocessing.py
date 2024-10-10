#!/usr/bin/python3

import multiprocessing
import numpy as np
import time, os

#load the simulation the monte_carlo.py file included in this repo
from monte_carlo import monte_carlo_simulation

def master_worker_pi_calculation(num_points, num_tasks):
    pool = multiprocessing.Pool(processes=num_tasks)
    batch_size = num_points // num_tasks
    results = pool.map(monte_carlo_simulation, [batch_size] * num_tasks)
    pool.close()
    pool.join()
    return sum(results)

if __name__ == "__main__":
    print('*'*35)
    print('running multiprocessing version of picalc')
    print('*'*35)

    # make sure this is the same across different examples if you wish to compare performance
    total_n_points = 100000 
    print('performing calculation with '+str(total_n_points)+' points')

    num_tasks = int(os.environ.get('SLURM_CPUS_ON_NODE', multiprocessing.cpu_count()))
    
    print('\nworking on',num_tasks,'processors\n')

    starttime = time.time()
    total_circle_count = master_worker_pi_calculation(total_n_points, num_tasks)
    endtime = time.time()

    pi_est = 4.0*total_circle_count/total_n_points
    percent_diff = (pi_est - np.pi)/np.pi * 100

    print('time taken to complete: {:.8f}s'.format(endtime - starttime))
    print('number of points generated: ',total_n_points)
    print('number of points in circle: ',total_circle_count)
    print('estimate of pi: ',pi_est)
    print('percent difference: ',np.round(percent_diff,2),'%')
