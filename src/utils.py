
import json
import os


def load_config(floc):
    fname = os.path.basename(floc)
    fname_woext = os.path.splitext(fname)[0]
    fname_ext = os.path.splitext(fname)[1]
    fdir = os.path.dirname(floc)
    
    floc_ext = os.path.join(fdir, fname_woext + '-ext' + fname_ext)
        
    # Load json config file and extension
    with open(floc) as json_file:
        config = json.load(json_file)

    if os.path.exists(floc_ext):
        with open(floc_ext) as json_file:
            extension = json.load(json_file)
        config = {**config, **extension}   
    return config