#!/usr/bin/python3

from mpi4py import MPI
import numpy as np
import time, os

total_n_points = 1000000#input("enter number of points [10,000]: ")
#try:
#    total_n_points = int(total_n_points)
#except:
#    total_n_points = 10000

print('performing calculation with '+str(total_n_points)+' points')

def monte_carlo_simulation(num):
    circle_count = 0

    for i in np.arange(num):
        new_point = np.array([2. * (np.random.random() - 0.5), 2 * (np.random.random() - 0.5)])

        if np.linalg.norm(new_point) < 1:
            circle_count += 1

    return circle_count

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

