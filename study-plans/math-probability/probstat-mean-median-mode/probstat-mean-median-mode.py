import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    mean_value = float(np.mean(x))
    median_value = float(np.median(x))

    counts = Counter(x)
    max_frequency = max(counts.values())

    mode_value = float(min([num for num, freq in counts.items() if freq == max_frequency]))

    return {'mean' : mean_value, 'median' : median_value, 'mode' : mode_value}
    
    pass