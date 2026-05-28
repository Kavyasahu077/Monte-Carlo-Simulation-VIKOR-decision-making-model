"""
Stores prior Beta distribution parameters
and historical operational data.
"""

components = {

    "Pump": {
        "alpha_prior": 1,
        "beta_prior": 1,
        "failures": 15,
        "trials": 1000
    },

    "Turbine": {
        "alpha_prior": 1,
        "beta_prior": 1,
        "failures": 1,
        "trials": 100
    },

    "Sensor": {
        "alpha_prior": 1,
        "beta_prior": 1,
        "failures": 10,
        "trials": 1000
    },

    "Valve": {
        "alpha_prior": 1,
        "beta_prior": 1,
        "failures": 4,
        "trials": 1000
    }
}