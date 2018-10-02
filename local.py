#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 2 11:25:00 2018 (MDT)

@author: Rogers F. Silva
"""

import json
import os
import sys
import numpy as np
import utils as ut
import local_ancillary as la


def local_1(args):

    state = args['state']
    inputs = args['input']
    cache = args['cache']

    ### Input data files
    file_list = inputs['data'][0]
    data_file_list = [os.path.join(state["baseDirectory"], file)
                      for file in file_list]
    data_file_type = inputs['data'][1][0]
    # Read local input data files
    datasets = ut.read_data(data_file_list, data_file_type, state['clientId'])
    
    ### Global Number of Principal Components
    num_PC_global = inputs['num_PC_global']

    ### Dimension to Be Reduced
    axis = inputs['axis']

    ### Define mean_removal tuple
    if axis == -1:
        ### Check if Global (Row) Mean Values provided
        file_list = inputs['mean_values'][0]
        if file_list:
            # Row mean files
            row_mean_file_list = [os.path.join(state["baseDirectory"], file)
                                for file in file_list]
            row_mean_file_type = inputs['row_mean_global'][1][0]
            # Read local row mean files
            row_mean = ut.read_data(row_mean_file_list, row_mean_file_type, state['clientId'])
        else:
            row_mean = None

        mean_removal = (axis, row_mean)
    elif axis == -2:
        ### Column means are always computed locally, on-the-fly
        mean_removal = (axis, None)
    
    ### Subject-Level PCA
    subject_level_PCA = inputs['subject_level_PCA']

    ### Number of Principal Components in Subject-Level PCA
    subject_level_num_PC = inputs['subject_level_num_PC']
    

    
    # Start local computation:

    

    # Compile results to be transmitted to remote and cached for reuse in next iteration
    computation_output = {
        "output": {
            "row_sum": row_sum.tolist(),
            "num_cols": num_cols,
            "row_sums": {ix:{"row_sum":X['row_sum'].tolist(), "num_cols":X['num_cols']}
                         for (ix,X) in row_sums.items()},
            "computation_phase": 'local_1'
        },
        "cache": dict()
    }

    return computation_output


# if __name__ == '__main__':

#     parsed_args = json.loads(sys.stdin.read())
#     phase_key = list(ut.listRecursive(parsed_args, 'computation_phase'))
    
#     if not phase_key:
#         computation_output = local_1(parsed_args)
#         # Transmit results to remote
#         # as file (for large volumes of data, OS overhead):
#         # as JSON string (for smaller volumes of data, JSON conversion overhead):
#         sys.stdout.write(json.dumps(computation_output))
#     else:
#         raise ValueError("Error occurred at Local")
