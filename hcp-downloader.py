import sys
import boto3
from creds import *
import os
import json

subj_prefix = lambda subj: f'sub-{subj}'
anat_file_name = lambda subj, mode: f'{subj_prefix(subj)}_{mode}w.nii.gz'
func_file_name = lambda subj: f'{subj_prefix(subj)}_task-rest_bold.nii.gz'

def make_folders_and_download(base_dir, subj, s3_bucket):
    subj_root_path = os.path.join(base_dir, subj_prefix(subj))

    '''
    BELOW CODE IS TO DOWNLOAD THE T1, T2 AND fMRI files
    The folders are structured to match BIDS. 
    '''
    anat_path = os.path.join(subj_root_path, 'anat')
    func_path = os.path.join(subj_root_path, 'func')

    # make root path
    os.makedirs(subj_root_path)

    # make anat and func folders
    os.makedirs(anat_path)
    os.makedirs(func_path)

    # download the t1 and t2 imgs
    s3_bucket.download_file(f'HCP_1200/{subj}/unprocessed/3T/T1w_MPR1/{subj}_3T_T1w_MPR1.nii.gz', os.path.join(anat_path, anat_file_name(subj, 'T1')))
    s3_bucket.download_file(f'HCP_1200/{subj}/unprocessed/3T/T2w_SPC1/{subj}_3T_T2w_SPC1.nii.gz', os.path.join(anat_path, anat_file_name(subj, 'T2')))

    # download the resting state fMRI
    s3_bucket.download_file(f'HCP_1200/{subj}/unprocessed/3T/rfMRI_REST1_LR/{subj}_3T_rfMRI_REST1_LR.nii.gz', os.path.join(func_path, func_file_name(subj)))

    # bids requires that we add this json file in the func directory
    with open(os.path.join(func_path ,f'sub-{subj}_task-rest_bold.json'), 'w') as f:
        json.dump({"TaskName": "Rest", "RepetitionTime": 0.720}, f)

    '''
    BELOW CODE IS TO DOWNLOAD DWI files
    '''
    diff_path = os.path.join(subj_root_path, 'dwi')

    os.makedirs(diff_path)

    s3_bucket.download_file(f'HCP_1200/{subj}/unprocessed/3T/Diffusion/{subj}_3T_DWI_dir95_LR.nii.gz', os.path.join(diff_path, f'sub-{subj}_dwi.nii.gz'))
    s3_bucket.download_file(f'HCP_1200/{subj}/unprocessed/3T/Diffusion/{subj}_3T_DWI_dir95_LR.bvec', os.path.join(diff_path, f'sub-{subj}_dwi.bvec'))
    s3_bucket.download_file(f'HCP_1200/{subj}/unprocessed/3T/Diffusion/{subj}_3T_DWI_dir95_LR.bval', os.path.join(diff_path, f'sub-{subj}_dwi.bval'))

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

s3 = session.resource('s3')
bucket = s3.Bucket('hcp-openaccess')

subject = sys.argv[1]
base_dir = os.path.join(os.environ["EPHEMERAL"], "fmri-input")

make_folders_and_download(base_dir, subject, bucket)
