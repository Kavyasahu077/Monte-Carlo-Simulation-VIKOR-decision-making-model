# Monte Carlo Simulation + Bayesian Network + VIKOR Decision-Making Model

## Overview
This project implements an integrated probabilistic decision-support framework using:

- Monte Carlo Simulation
- Bayesian Network Modeling
- Beta Distribution Updating
- Posterior Probability Analysis
- VIKOR Multi-Criteria Decision-Making (MCDM)

The system is designed for uncertainty analysis, reliability estimation, and intelligent decision-making in complex engineering systems.

# Project Structure

```bash
Monte Carlo Simulation + VIKOR decision-making model/
│
├── main.py
├── config.py
├── requirements.txt
│
├── data/
│   ├── __init__.py
│   ├── prior_data.py
│   ├── criteria_data.py
│   └── ahp_matrix.py
│
├── bayesian_network/
│   ├── __init__.py
│   ├── bayes_model.py
│   ├── beta_update.py
│   └── posterior_analysis.py

# Features

- Probabilistic Bayesian modeling
- Monte Carlo-based uncertainty simulation
- Beta distribution updating
- Posterior probability estimation
- VIKOR-based decision ranking
- Modular Python architecture
- Research-oriented implementation

---

# Technologies Used

- Python 3.x
- NumPy
- Pandas
- SciPy
- Matplotlib

---

# Workflow

## 1. Data Input

The user provides:

- Component information
- Failure probabilities
- Success probabilities
- Criteria weights
- Prior probabilities

---

## 2. Bayesian Network Modeling

The Bayesian model:

- Represents dependencies
- Computes conditional probabilities
- Updates beliefs dynamically

### Implemented in:

```python
bayesian_network/bayes_model.py
