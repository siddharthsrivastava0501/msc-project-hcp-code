#!/bin/bash
#PBS -lselect=1:ncpus=10:mem=16gb
#PBS -lwalltime=02:00:00
#PBS -J 5-99

cd $PBS_O_WORKDIR

SUBJ_ID=$(sed "${PBS_ARRAY_INDEX}q;d" 100-unrelated_subject_id.txt)

mkdir -p $TMPDIR/fmri-input
cp -r $EPHEMERAL/fmri-input/sub-${SUBJ_ID} $TMPDIR/fmri-input
cp $EPHEMERAL/fmri-input/dataset_description.json $TMPDIR/fmri-input/

singularity run --cleanenv -B $TMPDIR:/data /rds/general/user/ss2620/home/my-images/nipreps_fmriprep_23.2.2-2024-05-06-cd14edecb89c.simg \
/data/fmri-input /data/fmri-derivatives/ \
participant --participant-label $SUBJ_ID --skip-bids-validation --mem 16000 --fs-no-reconall --fs-license-file $HOME/msc-project-code/license.txt 


mkdir -p $EPHEMERAL/fmri-outputs/sub-${SUBJ_ID}/
cp -r $TMPDIR/fmri-derivatives/. $EPHEMERAL/fmri-outputs/sub-${SUBJ_ID}/