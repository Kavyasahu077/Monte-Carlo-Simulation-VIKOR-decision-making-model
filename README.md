# Monte Carlo Simulation + Bayesian Network + VIKOR Decision-Making Model

## Overview

This project implements an integrated probabilistic decision-support framework using:

- Monte Carlo Simulation
- Bayesian Network Modeling
- Beta Distribution Updating
- Posterior Probability Analysis
- VIKOR Multi-Criteria Decision-Making (MCDM)

The system is designed for uncertainty analysis, reliability estimation, and intelligent decision-making in complex engineering systems.

---

# Project Structure

```text
Monte_Carlo_Simulation_VIKOR_Model/
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
```

---

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

### Implemented In

```python
bayesian_network/bayes_model.py
```

---

## 3. Beta Distribution Updating

The system updates prior beliefs using Beta distribution functions.

### Formula

\[
P(\theta | x) \propto P(x | \theta) \cdot P(\theta)
\]

### Implemented In

```python
bayesian_network/beta_update.py
```

---

## 4. Monte Carlo Simulation

Monte Carlo simulation is used to:

- Handle uncertainty
- Generate random probabilistic samples
- Estimate reliability distributions
- Support stochastic analysis

---

## 5. Posterior Probability Analysis

Posterior distributions are analyzed for:

- Risk estimation
- Reliability prediction
- Decision confidence measurement

### Implemented In

```python
bayesian_network/posterior_analysis.py
```

---

## 6. VIKOR Decision-Making

The VIKOR method ranks alternatives based on:

- Multiple conflicting criteria
- Weighted decision matrices
- Compromise solutions

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

Move into the project directory:

```bash
cd Monte_Carlo_Simulation_VIKOR_Model
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

```bash
python main.py
```

---

# Future Improvements

- GUI integration
- Real-time data support
- Advanced Bayesian inference
- AI-assisted optimization
- Sensitivity analysis dashboards

---

# License

This project is intended for research and educational purposes.
