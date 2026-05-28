"""
Bayesian sampling model using Beta distribution.
"""

import numpy as np


def sample_failure_probability(alpha, beta):
    """
    Samples stochastic failure probability
    from Beta distribution.
    """

    return np.random.beta(alpha, beta)