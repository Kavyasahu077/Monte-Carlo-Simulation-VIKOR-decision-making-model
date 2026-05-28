"""
Main execution pipeline for Bayesian
Monte Carlo simulation framework.
"""

from data.prior_data import components
from data.criteria_data import criteria_values

from bayesian_network.beta_update import update_beta

from bayesian_network.bayes_model import (
    sample_failure_probability
)

from bayesian_network.posterior_analysis import (
    posterior_mean,
    posterior_variance
)


def main():

    print("\n===== Bayesian Monte Carlo Pipeline =====\n")

    for component_name, values in components.items():

        # Prior parameters
        alpha_prior = values["alpha_prior"]
        beta_prior = values["beta_prior"]

        # Historical data
        failures = values["failures"]
        trials = values["trials"]

        # Bayesian updating
        alpha_post, beta_post = update_beta(
            alpha_prior,
            beta_prior,
            failures,
            trials
        )

        # Posterior statistics
        mean_probability = posterior_mean(
            alpha_post,
            beta_post
        )

        variance_probability = posterior_variance(
            alpha_post,
            beta_post
        )

        # Monte Carlo Beta sampling
        sampled_probability = sample_failure_probability(
            alpha_post,
            beta_post
        )

        # Deterministic criteria
        severity = criteria_values[component_name][
            "severity"
        ]

        detectability = criteria_values[
            component_name
        ]["detectability"]

        # Display results
        print(f"Component: {component_name}")

        print(
            f"Posterior Distribution: "
            f"Beta({alpha_post}, {beta_post})"
        )

        print(
            f"Posterior Mean: "
            f"{mean_probability:.6f}"
        )

        print(
            f"Posterior Variance: "
            f"{variance_probability:.10f}"
        )

        print(
            f"Sampled Failure Probability: "
            f"{sampled_probability:.6f}"
        )

        print(f"Severity: {severity}")

        print(f"Detectability: {detectability}")

        print("-" * 60)


if __name__ == "__main__":
    main()