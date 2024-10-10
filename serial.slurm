#!/bin/bash
# --------------------
### Directives Section
# --------------------
#SBATCH --job-name=picalc-serial
#SBATCH --account=ejahn
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH -o picalc-serial-%j.out
#SBATCH -e picalc-serial-%j.err

# --------------------
### Code Section
# --------------------
module load python/3.11
source ~/pip/picalc/bin/activate

cd ~/picalc_example
python3 picalc_serial.py