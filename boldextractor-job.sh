#!/bin/bash
#PBS -l select=1:ncpus=4:mem=16gb
#PBS -l walltime=00:10:00
#PBS -J 1-100

module load tools/prod
module load Python/3.11.3-GCCcore-12.3.0
source ~/msc-project-code/venv/bin/activate

cd $PBS_O_WORKDIR

SUBJ_ID=$(sed "${PBS_ARRAY_INDEX}q;d" 100-unrelated_subject_id.txt)

python3 bold-extractor.py \
$HOME/fmri-outputs/sub-${SUBJ_ID}/sub-${SUBJ_ID}/func/sub-${SUBJ_ID}_task-rest_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz \
$HOME/fmri-outputs/sub-${SUBJ_ID}/sub-${SUBJ_ID}_task-rest_bold_Scahefer100x7_normalised.npy