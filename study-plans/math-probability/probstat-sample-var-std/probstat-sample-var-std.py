import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    """
    # mean
    mean_value = float(np.mean(x))
    variance_value = float(np.var(x, ddof=1))
    stddev_value = float(np.std(x, ddof=1))

    return {'variance' : variance_value, 'std_dev' : stddev_value}