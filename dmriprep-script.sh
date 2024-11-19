#!/bin/bash
#PBS -lselect=1:ncpus=10:mem=30gb
#PBS -lwalltime=12:00:00

cd $PBS_O_WORKDIR

SUBJ_ID=$(sed "${PBS_ARRAY_INDEX}q;d" 100-unrelated_subject_id.txt)
SUBJ_ID=100307

mkdir -p $TMPDIR/fmri-input
cp -r $EPHEMERAL/fmri-input/sub-${SUBJ_ID} $TMPDIR/dmri-input
cp $EPHEMERAL/fmri-input/dataset_description.json $TMPDIR/dmri-input/

singularity run --cleanenv -B $TMPDIR:/data /rds/general/user/ss2620/home/my-images/nipreps_dmriprep_latest-2021-03-11-34262b8fafb6.simg \
/data/dmri-input /data/dmri-derivatives/ \
participant --participant-label $SUBJ_ID --skip-bids-validation --mem 30 --low-mem --fs-license-file $HOME/msc-project-code/license.txt 

mkdir -p $HOME/dmri-outputs/sub-${SUBJ_ID}/
cp -r $TMPDIR/dmri-derivatives/ $HOME/dmri-outputs/sub-${SUBJ_ID}/q