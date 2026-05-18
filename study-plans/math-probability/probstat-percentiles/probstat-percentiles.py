import numpy as np

def percentiles(x, q):
    """
    Returns: numpy array of percentile values.
    """
    percentile = np.percentile(x, q)
    
    return percentile
