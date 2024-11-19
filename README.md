## Physics-Informed Factor Graphs for Learning in Complex Dynamical Systems
### HCP Processing Code
#### Author: Siddharth Srivastava

This code downlodas structural, functional and dMRI files from 100 unrelated subjects in the Human Connectome Project (HCP). 

To use this repository, you will have to acquire S3 credentials from the AWS website and place them in `creds.py`. 

You will also have to acquire the `license.txt` for FreeSurfer from fMRIprep to process the download functional data. 

Lastly, you will have to download the singularity images for both `dmriprep` and `fmriprep` to use the batch processing scripts on the Imperial RCS. 