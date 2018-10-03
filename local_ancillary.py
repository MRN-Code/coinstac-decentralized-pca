#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 2 20:19:00 2018 (MDT)

@author: Rogers F. Silva
"""

import numpy as np
import ancillary as an

def local_PCA(site,
              num_PC,
              mean_removal=None,
              subject_level_PCA=True,
              subject_level_num_PC=120):
    """ Local PCA

    Local principal component analysis method for dPCA.
    Accounts for mean removal and subject-level whitening.
    """
    subject_list = site.keys()
    data_subject = np.array([])
    projM = {}
    bkprojM = {}
    for mm in subject_list:
        raw_subject = site[mm]

        if mean_removal:
            axis, mean_values = mean_removal  # mean_removal is a tuple
            if axis == -2:
                # Remove column means
                # Ignore contents of mean_values
                raw_subject = raw_subject - np.mean(raw_subject, axis=0)
            elif axis == -1:
                # Remove row means
                # mean_values computed in decentralized fashion elsewhere
                raw_subject = raw_subject - mean_values[:, None]

        if subject_level_PCA:
            # This is subject level PCA with whitening
            data_subject_tmp, projM[mm], bkprojM[mm] = an.base_PCA(
                raw_subject,
                num_PC=subject_level_num_PC,
                axis=1,
                whitening=True)
            data_subject = np.hstack(
                (data_subject,
                 data_subject_tmp)) if data_subject.size else data_subject_tmp
        else:
            data_subject = np.hstack(
                (data_subject,
                 raw_subject)) if data_subject.size else raw_subject

    reduced_data, _, _ = an.base_PCA(
        data_subject, num_PC=num_PC, axis=1, whitening=False)
    return reduced_data, projM, bkprojM