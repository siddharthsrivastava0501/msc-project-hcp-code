from nilearn import datasets
from nilearn.maskers import NiftiLabelsMasker
import numpy as np
import os
import sys

data_path = sys.argv[1]
out_path = sys.argv[2]

atlas = datasets.fetch_atlas_schaefer_2018(n_rois = 100, yeo_networks = 7, resolution_mm=1)

masker = NiftiLabelsMasker(
    atlas.maps,
    labels = np.insert(atlas.labels, 0, 'Background'.encode('UTF-8')),
    background_label=0.0,
    standardize='zscore'
)

signals = masker.fit_transform(data_path)

np.save(out_path, signals)