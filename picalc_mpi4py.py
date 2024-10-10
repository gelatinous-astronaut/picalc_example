#!/usr/bin/python3

from mpi4py import MPI
import numpy as np
import time, os

#load the simulation the monte_carlo.py file included in this repo
from monte_carlo import monte_carlo_simulation

def master_worker_pi_calculation(num_points, num_tasks):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        total_circle_count = 0
        batch_size = num_points // (size - 1)

        for i in range(1, size):
            comm.send(batch_size, dest=i)

        for i in range(1, size):
            total_circle_count += comm.recv(source=i)

        return total_circle_count
    else:
        batch_size = comm.recv(source=0)
        task_count = monte_carlo_simulation(batch_size)
        comm.send(task_count, dest=0)

if __name__ == "__main__":
    print('*'*35)
    print('running mpi4py version of picalc')
    print('*'*35)

    # make sure this is the same across different examples if you wish to compare performance
    total_n_points = 100000 
    print('performing calculation with '+str(total_n_points)+' points')

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        num_tasks = int(os.environ.get('SLURM_NTASKS'))
        print('\nworking on', num_tasks, 'processors\n')

        starttime = time.time()
        total_circle_count = master_worker_pi_calculation(total_n_points, num_tasks)
        endtime = time.time()

        pi_est = 4.0 * total_circle_count / total_n_points
        percent_diff = (pi_est - np.pi) / np.pi * 100

        print('time taken to complete: {:.8f}s'.format(endtime - starttime))
        print('number of points generated: ', total_n_points)
        print('number of points in circle: ', total_circle_count)
        print('estimate of pi: ', pi_est)
        print('percent difference: ', np.round(percent_diff, 2), '%')
    else:
        master_worker_pi_calculation(None, None)

