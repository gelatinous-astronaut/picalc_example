#!/bin/bash
# --------------------
### Directives Section
# --------------------
#SBATCH --job-name=picalc-multiproc
#SBATCH --account=ejahn
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8 ###change this to see how the time taken changes!
#SBATCH --time=00:10:00
#SBATCH -o picalc-multiproc-%j.out
#SBATCH -e picalc-multiproc-%j.err

# --------------------
### Code Section
# --------------------
module load python/3.11
source ~/pip/picalc/bin/activate

cd ~/picalc_example
python3 picalc_multiprocessing.py