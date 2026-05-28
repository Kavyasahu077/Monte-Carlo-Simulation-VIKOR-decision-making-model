"""
Performs Bayesian posterior parameter updating.
"""


def update_beta(alpha_prior, beta_prior, failures, trials):
    """
    Updates posterior Beta distribution parameters.
    """

    successes = trials - failures

    alpha_post = alpha_prior + failures
    beta_post = beta_prior + successes

    return alpha_post, beta_post