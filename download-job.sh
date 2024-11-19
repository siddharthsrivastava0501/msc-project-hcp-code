#!/bin/bash
#PBS -l select=1:ncpus=1:mem=1gb
#PBS -l walltime=00:15:00
#PBS -J 1-2


module load tools/prod
module load Python/3.11.3-GCCcore-12.3.0
source ~/msc-project-code/venv/bin/activate

cd $PBS_O_WORKDIR

python3 hcp-downloader.py $(sed "${PBS_ARRAY_INDEX}q;d" 100-unrelated_subject_id.txt)