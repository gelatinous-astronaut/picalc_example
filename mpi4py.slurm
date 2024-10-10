#!/bin/bash
# --------------------
### Directives Section
# --------------------
#SBATCH --job-name=picalc-mpi4py
#SBATCH --account=ejahn
#SBATCH --partition=standard
#SBATCH --nodes=3
#SBATCH --ntasks=12				### 12 CPUs spread across 3 nodes
#SBATCH --ntasks-per-node=4
#SBATCH --time=00:10:00
#SBATCH -o picalc-mpi4py-%j.out
#SBATCH -e picalc-mpi4py-%j.err

# --------------------
### Code Section
# --------------------
module load python/3.11
source ~/pip/picalc/bin/activate

cd ~/picalc_example
mpirun -n $SLURM_NTASKS python3 picalc_multiprocessing.py