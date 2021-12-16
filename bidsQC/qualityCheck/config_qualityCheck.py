import os
from datetime import datetime
from sequence import Sequence
from timepoint import TimePoint

######################## CONFIGURABLE PART BELOW ########################

# Set directories (Check these for your study)
# These variables are used in the main script and need to be defined here. 
# They need to exist prior to running the qualityCheck.py
path_bidsdata = os.path.join(os.sep, 'projects', "sanlab", 'shared', "ctnTutorial", 'bids_data')  # Where your subjects' nifti directories are
logdir = os.path.join(os.getcwd(), 'logs_qualityCheck')  # Log files will go in the folder from which this script is run

# Create a dictionary (the thing below) for each timepoint in your study.
sequence1 = Sequence("func", {"bart": 1, "gng1":1, "gng2":1, "react1":1, "react2":1, "sst1":1, "sst2":1})
sequence2 = Sequence("func", {"bart": 1, "gng3":1, "gng4":1, "react3":1, "react4":1, "sst3":1, "sst4":1})
sequence3 = Sequence("anat", {"T1w":1})
sequence4 = Sequence("fmap", {"magnitude1":2, "magnitude2":2, "phasediff":2 })
timepoint1 = TimePoint("ses-wave1", [sequence1, sequence3, sequence4])
timepoint2 = TimePoint("ses-wave2", [sequence2, sequence3, sequence4])
expected_timepoints = [timepoint1, timepoint2]

# Files g-zipped or not?
# NOTE: All files must be either zipped or unzipped. 
# A mixture won't work properly.
gzipped = True

# If you have different versions of the same task - e.g. stopsignal was run twice with different images
# And those runs were named differently - e.g. stopsignalA and stopsignalB
# You need them to be recognized as multiple runs of the same task. 
# List them below to have the 'run-#' field appended to indicate the order in which they were run.
order_sequences = True
tasks_to_order = 'gng', 'react', 'sst'  # comma seperated if multiple


######################## DO NOT CHANGE ########################
tempdir = os.path.join(path_bidsdata, 'tmp_dcm2bids')  # holding folder for undesired files
outputlog = os.path.join(logdir, 'outputlog_qualityCheck' + datetime.now().strftime('%Y%m%d-%H%M%S') + '.txt')
errorlog = os.path.join(logdir, 'errorlog_qualityCheck' + datetime.now().strftime('%Y%m%d-%H%M%S') + '.txt')
derivatives = os.path.join(path_bidsdata, 'derivatives')  # Where processed data will go