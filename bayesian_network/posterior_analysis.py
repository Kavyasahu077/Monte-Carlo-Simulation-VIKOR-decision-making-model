"""
Posterior distribution analysis utilities.
"""


def posterior_mean(alpha, beta):
    """
    Computes posterior mean.
    """

    return alpha / (alpha + beta)


def posterior_variance(alpha, beta):
    """
    Computes posterior variance.
    """

    numerator = alpha * beta

    denominator = (
        (alpha + beta) ** 2
        * (alpha + beta + 1)
    )

    return numerator / denominator